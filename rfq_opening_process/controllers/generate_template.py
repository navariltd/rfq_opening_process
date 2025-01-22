from collections import defaultdict
from datetime import datetime
import os
import base64

import frappe
from frappe.query_builder import DocType


from datetime import datetime


def format_date_with_ordinal(date_obj):
    day = date_obj.day
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    formatted_date = date_obj.strftime(f"%d{suffix} %B, %Y")
    return formatted_date


def get_signature_image(member_data):
    public_path = frappe.utils.get_site_path("public", "files")

    if member_data:
        image_name = (
            f"{member_data.get('full_name', 'image').replace(' ','_').lower()}.png"
        )
        base64_image = member_data.get("signature")
        if base64_image.startswith("data:image/png;base64,"):
            base64_image = base64_image.replace("data:image/png;base64,", "")

        full_file_path = os.path.join(public_path, image_name)

        with open(full_file_path, "wb") as fh:
            fh.write(base64.b64decode(base64_image))

        file_record = frappe.get_doc(
            {
                "doctype": "File",
                "file_name": image_name,
                "file_url": f"/files/{image_name}",
                "attached_to_name": "Test Name",
                "attached_to_doctype": "Committee",
                "file_size": os.path.getsize(full_file_path),
                "is_private": 0,
                "file_type": "PNG",
            }
        )

        file_record.insert()

        return f"/files/{image_name}"


def get_supplier_quotations(rfq):
    sq = DocType("Supplier Quotation")
    sq_item = DocType("Supplier Quotation Item")

    query = (
        frappe.qb.from_(sq_item)
        .from_(sq)
        .select(sq.supplier.as_("supplier_name"), sq_item.request_for_quotation)
        .where(
            (sq_item.parent == sq.name)
            & (sq_item.docstatus < 2)
            & (sq_item.request_for_quotation == rfq)
        )
    )

    supplier_quotation_data = query.run(as_dict=True)

    supplier_dict = defaultdict(lambda: {"supplier_name": ""})

    if supplier_quotation_data:
        for data in supplier_quotation_data:
            key = data.supplier_name
            supplier_dict[key]["supplier_name"] = data.get("supplier_name")

    supplier_quotation_data = supplier_dict.values()
    return supplier_quotation_data


def get_purchase_intent_note(rfq):
    rfq_item = DocType("Request for Quotation Item")

    query = (
        frappe.qb.from_(rfq_item)
        .select(rfq_item.material_request.as_("purchase_intent_note"))
        .where(rfq_item.parent == rfq)
    )

    pi_note = query.run(as_dict=True)
    pi_dict = defaultdict(lambda: {"purchase_intent_note": ""})
    pi_title = ""

    if pi_note:
        for data in pi_note:
            key = data.purchase_intent_note
            pi_dict[key]["purchase_intent_note"] = data.get(
                "purchase_intent_note", None
            )

        pi_note = list(pi_dict.values())
        first_pi_note = pi_note[0].get("purchase_intent_note")
        pi_doc = (
            frappe.get_doc("Material Request", first_pi_note)
            if first_pi_note is not None
            else None
        )
        pi_title = pi_doc.title if pi_doc else None

    return pi_note, pi_title


@frappe.whitelist()
def generate_template(quotation, note_type, date):
    supplier_quotations = get_supplier_quotations(quotation)

    rfq_doc = frappe.get_doc("Request for Quotation", quotation)
    committee_members = (
        frappe.db.get_all(
            "Committee Member",
            filters={"parent": rfq_doc.committee},
            fields=["name"],
        )
        if rfq_doc.committee
        else None
    )

    committee_data = []
    if committee_members:
        for member in committee_members:
            member_data = frappe.db.get_value(
                "Committee Member",
                filters={"name": member.name},
                fieldname=["full_name", "signature"],
                as_dict=1,
            )
            # signature_img = get_signature_image(member_data)
            # if signature_img:
            #     frappe.log_error(signature_img)
            #     member_data["signature_img"] = signature_img
            committee_data.append(member_data)

    context = defaultdict()

    date_obj = datetime.strptime(date, "%Y-%m-%d")
    new_date = date_obj.strftime("%d/%m/%Y")

    context["date"] = new_date
    context["rfq_name"] = rfq_doc.name
    context["transaction_date"] = format_date_with_ordinal(
        datetime.strptime(rfq_doc.get_formatted("transaction_date"), "%d-%m-%Y")
    )
    context["closing_date"] = format_date_with_ordinal(
        datetime.strptime(rfq_doc.get_formatted("closing_date"), "%d-%m-%Y")
    )
    context["committee_members"] = committee_data
    context["supplier_quotations"] = (
        supplier_quotations if supplier_quotations else None
    )
    context["no_of_suppliers"] = len(supplier_quotations) if supplier_quotations else 0

    template_path = "templates/includes"
    rendered_content = ""

    if note_type == "Opening Minutes":
        _, pi_title = get_purchase_intent_note(quotation)
        context["pi_title"] = pi_title if pi_title else None

        rendered_content = frappe.render_template(
            f"{template_path}/rfq_opening_minutes.html", context=context
        )

    elif note_type == "Evaluation Minutes":
        pi_notes, pi_title = get_purchase_intent_note(quotation)
        context["pi_note"] = pi_notes[0]
        context["pi_title"] = pi_title if pi_title else None

        rendered_content = frappe.render_template(
            f"{template_path}/rfq_evaluation_minutes.html", context=context
        )
    else:
        _, pi_title = get_purchase_intent_note(quotation)
        context["pi_title"] = pi_title if pi_title else None
        rendered_content = frappe.render_template(
            f"{template_path}/rfq_committee_register.html", context=context
        )

    frappe.response["message"] = rendered_content
