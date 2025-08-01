import frappe, feature_tracker
from frappe import _
from frappe.utils import getdate
from typing import Dict, Optional
import json



def validate_permission(permission_type: str, doc_name: Optional[str] = None) -> None:
    """Validate user permissions for Feature Request doctype"""
    if not frappe.has_permission("Feature Request", permission_type, doc_name):
        frappe.throw(_(feature_tracker.ERRORS.get("no_read_permission")), frappe.PermissionError)


def validate_document_exists(name: str) -> None:
    """Validate that a Feature Request document exists"""
    if not frappe.db.exists("Feature Request", name):
        frappe.throw(_(feature_tracker.ERRORS.get("feature_request_not_exist")).format(name), frappe.DoesNotExistError)


def validate_required_field(value: str, field_name: str) -> None:
    """Validate that a required field is not empty"""
    if not value or not value.strip():
        frappe.throw(_(feature_tracker.ERRORS.get("field_required")).format(field_name), frappe.ValidationError)


def validate_choice_field(value: str, field_name: str, valid_choices: list) -> None:
    """Validate that a field value is from the allowed choices"""
    if value not in valid_choices:
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_choice")).format(field_name, ", ".join(valid_choices)), frappe.ValidationError)


def validate_date_format(date_str: str) -> None:
    """Validate date format"""
    try:
        getdate(date_str)
    except Exception:
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_date_format")), frappe.ValidationError)


def parse_filters(filters: Optional[str]) -> Dict:
    """Parse and validate filters parameter"""
    if not filters:
        return {}
    
    try:
        return json.loads(filters) if isinstance(filters, str) else filters
    except (json.JSONDecodeError, TypeError):
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_filters_format")), frappe.ValidationError)


def build_search_filters(search: str, existing_filters: Dict) -> Dict:
    """Build search filters for title and description"""
    search_term = f'%{search}%'
    
    if existing_filters:
        # Combine with existing filters using AND
        return {**existing_filters, 'title': ['like', search_term]}
    else:
        # Use OR condition for title and description search
        return [
            ['title', 'like', search_term],
            ['description', 'like', search_term]
        ]


def get_pagination_info(total_count: int, limit_start: int, limit_page_length: int) -> Dict:
    """Calculate pagination information"""
    total_pages = (total_count + limit_page_length - 1) // limit_page_length
    current_page = (limit_start // limit_page_length) + 1
    
    return {
        'current_page': current_page,
        'total_pages': total_pages,
        'limit_start': limit_start,
        'limit_page_length': limit_page_length,
        'has_next': current_page < total_pages,
        'has_previous': current_page > 1
    }

def get_doctype_meta(doctype: str):
    """Get doctype metadata with caching for performance"""
    return frappe.get_meta(doctype)


def get_default_fields(doctype: str, exclude_fields: list = ["amended_from"], include_fields: list = ["name", 'creation', 'modified', 'owner', 'modified_by']) -> list:
    """Get list of visible, non-break fields from doctype metadata"""
    meta = get_doctype_meta(doctype)
    
    # Get all fields that are not break fields, not hidden, and have fieldnames
    default_fields = [
        df.fieldname for df in meta.fields
        if (df.fieldtype not in ["Section Break", "Column Break", "Tab Break"] and
            not df.hidden and
            df.fieldname and
            df.fieldname not in exclude_fields)
    ]
    
    return include_fields + default_fields


def get_choice_options(doctype: str, fieldname: str) -> list:
    """Get choice options for a select/choice field from doctype metadata"""
    meta = get_doctype_meta(doctype)
    field = meta.get_field(fieldname)
    
    if field and field.options:
        return field.options.splitlines()
    
    return []