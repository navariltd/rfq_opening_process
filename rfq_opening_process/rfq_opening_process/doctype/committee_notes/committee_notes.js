// Copyright (c) 2025, Navari Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on("Committee Notes", {
  //   refresh(frm) {
  //     if (frm.doc.template_name && frm.doc.quotation) {
  //       frm.add_custom_button("Generate Content", function () {
  //         frappe.call({
  //           method:
  //             "rfq_opening_process.controllers.generate_template.generate_template",
  //           args: {
  //             template_name: frm.doc.template_name,
  //             quotation: frm.doc.quotation,
  //             context: {
  //               name: frm.doc.name,
  //             },
  //           },
  //           callback: function (res) {
  //             if (res && res.message) {
  //               content = res.message;
  //               //   frappe.msgprint(res.message);
  //               frm.set_value("generated_content", content);
  //             }
  //           },
  //         });
  //       });
  //     }
  //   },
  note_type(frm) {
    if (frm.doc.quotation && frm.doc.note_type) {
      frappe.call({
        method:
          "rfq_opening_process.controllers.generate_template.generate_template",
        args: {
          quotation: frm.doc.quotation,
          note_type: frm.doc.note_type,
          context: {
            name: frm.doc.name,
          },
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
