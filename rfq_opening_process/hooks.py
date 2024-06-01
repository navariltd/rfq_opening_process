from . import __version__ as app_version
from erpnext.buying.doctype.request_for_quotation.request_for_quotation import (
    RequestforQuotation,
)
from .rfq_opening_process.doctype.request_for_quotation.request_for_quotation import (
    send_to_supplier,
)

app_name = "rfq_opening_process"
app_title = "Navari RFQ Opening Process"
app_publisher = "Navari Limited"
app_description = "ERPNext Extensions on Request for Quotation and Supplier Quotation to include Committee Bid Openings"
app_email = "info@navari.co.ke"
app_license = "GNU General Public License (v3)"
required_apps = ["frappe/erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rfq_opening_process/css/rfq_opening_process.css"
# app_include_js = "/assets/rfq_opening_process/js/rfq_opening_process.js"

# include js, css files in header of web template
# web_include_css = "/assets/rfq_opening_process/css/rfq_opening_process.css"
# web_include_js = "/assets/rfq_opening_process/js/rfq_opening_process.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rfq_opening_process/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "ToDo": "public/js/todo.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "rfq_opening_process.utils.jinja_methods",
# 	"filters": "rfq_opening_process.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rfq_opening_process.install.before_install"
# after_install = "rfq_opening_process.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rfq_opening_process.uninstall.before_uninstall"
# after_uninstall = "rfq_opening_process.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rfq_opening_process.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
    "Supplier Quotation": "rfq_opening_process.rfq_opening_process.doctype.supplier_quotation.supplier_quotation.get_permission_query_conditions",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rfq_opening_process.tasks.all"
# 	],
# 	"daily": [
# 		"rfq_opening_process.tasks.daily"
# 	],
# 	"hourly": [
# 		"rfq_opening_process.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rfq_opening_process.tasks.weekly"
# 	],
# 	"monthly": [
# 		"rfq_opening_process.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "rfq_opening_process.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    # "frappe.desk.doctype.event.event.get_events": "rfq_opening_process.event.get_events",
    "erpnext.buying.doctype.request_for_quotation.request_for_quotation.create_supplier_quotation": "rfq_opening_process.rfq_opening_process.doctype.request_for_quotation.request_for_quotation.create_supplier_quotation_override",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rfq_opening_process.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

RequestforQuotation.send_to_supplier = send_to_supplier

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rfq_opening_process.auth.validate"
# ]
