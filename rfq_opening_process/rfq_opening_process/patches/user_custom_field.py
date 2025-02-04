import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    custom_fields = {
        "User": [
            {
                "fieldname": "signature",
                "fieldtype": "Attach",
                "label": "Signature",
                "insert_after": "mobile_no",
                "translatable": 1,
            }
        ]
    }
    create_custom_fields(custom_fields, update=True)
