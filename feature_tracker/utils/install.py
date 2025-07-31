import frappe

def after_install():
	print("Running Feature Tracker After Install Hook")
	set_website_settings()

def after_migrate():
	print("Running Feature Tracker After Migrate Hook")
	set_app_logo()

def set_app_logo():
	# Sets app logo of installed apps through hooks
	print("Setting App Logo")
	app_logo = frappe.get_hooks("app_logo_url")[-1]
	frappe.db.set_single_value("Navbar Settings", "app_logo", app_logo)

def set_website_settings():
	 # Sets the default website settings
	print("Setting Default Website Settings")
	settings = frappe.get_doc("Website Settings")
	settings.app_name = "InnoSoft"
	settings.home_page = "login"
	settings.hide_footer_signup = True
	settings.save()


