app_name = "feature_tracker"
app_title = "Feature Tracker"
app_publisher = "Mohamed Amir"
app_description = "An internal feature tracking tool built with Frappe, designed to help teams monitor the development progress of product features."
app_email = "mohamedamirr424@gmail.com"
app_license = "mit"

# Website Context & Branding
# ----------

app_logo_url = "/assets/feature_tracker/images/branding/logo.png"

website_context = {
	"favicon": "/assets/feature_tracker/images/branding/favicon.png",
	"splash_image": "/assets/feature_tracker/images/branding/logo.png"
}


# Installation
# ------------

after_install = "feature_tracker.utils.install.after_install"
after_migrate = "feature_tracker.utils.install.after_migrate"

# Fixtures
# ------------

fixtures = [
	"Workflow",
    "Workflow State",
    "Workflow Action Master",
]

# Svg Icons
# ------------------
# include app icons in desk
app_include_icons = [
    "feature_tracker/icons/my_custom_icons.svg"
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "feature_tracker",
# 		"logo": "/assets/feature_tracker/logo.png",
# 		"title": "Feature Tracker",
# 		"route": "/feature_tracker",
# 		"has_permission": "feature_tracker.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/feature_tracker/css/feature_tracker.css"
# app_include_js = "/assets/feature_tracker/js/feature_tracker.js"

# include js, css files in header of web template
# web_include_css = "/assets/feature_tracker/css/feature_tracker.css"
# web_include_js = "/assets/feature_tracker/js/feature_tracker.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "feature_tracker/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
# 	"methods": "feature_tracker.utils.jinja_methods",
# 	"filters": "feature_tracker.utils.jinja_filters"
# }

# Uninstallation
# ------------

# before_uninstall = "feature_tracker.uninstall.before_uninstall"
# after_uninstall = "feature_tracker.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "feature_tracker.utils.before_app_install"
# after_app_install = "feature_tracker.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "feature_tracker.utils.before_app_uninstall"
# after_app_uninstall = "feature_tracker.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "feature_tracker.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
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
# 		"feature_tracker.tasks.all"
# 	],
# 	"daily": [
# 		"feature_tracker.tasks.daily"
# 	],
# 	"hourly": [
# 		"feature_tracker.tasks.hourly"
# 	],
# 	"weekly": [
# 		"feature_tracker.tasks.weekly"
# 	],
# 	"monthly": [
# 		"feature_tracker.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "feature_tracker.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "feature_tracker.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "feature_tracker.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["feature_tracker.utils.before_request"]
# after_request = ["feature_tracker.utils.after_request"]

# Job Events
# ----------
# before_job = ["feature_tracker.utils.before_job"]
# after_job = ["feature_tracker.utils.after_job"]

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

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"feature_tracker.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

