// Copyright (c) 2025, Navari Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on("Committee Notes", {
  note_type(frm) {
    if (frm.doc.quotation && frm.doc.note_type) {
      frappe.call({
        method:
          "rfq_opening_process.controllers.generate_template.generate_template",
        args: {
          quotation: frm.doc.quotation,
          note_type: frm.doc.note_type,
          date: frm.doc.posting_date,
        },
        callback: function (res) {
          if (res && res.message) {
            content = res.message;
            frm.set_value("generated_content", content);
          }
        },
      });
    }
  },
});
