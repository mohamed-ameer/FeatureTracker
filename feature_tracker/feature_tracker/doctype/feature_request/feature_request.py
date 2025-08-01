# Copyright (c) 2025, Mohamed Amir and contributors
# For license information, please see license.txt

# import frappe
import frappe, feature_tracker
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_date_str, today

class FeatureRequest(Document):
	def validate(self):
		self.validate_date()

	def validate_date(self):
		# Validate that the date is today for a new feature request
		# Only validate on creation
		if self.is_new():
			if get_date_str(self.date) != today():
				frappe.throw(_(feature_tracker.ERRORS.get("invalid_date")))
