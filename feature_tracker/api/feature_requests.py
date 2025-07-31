"""
Feature Request CRUD API

This module provides comprehensive CRUD operations for Feature Request doctype
with proper authentication, validation, and error handling.

API Endpoints:
- GET /api/method/feature_tracker.api.feature_requests.get_feature_requests - List all feature requests
- GET /api/method/feature_tracker.api.feature_requests.get_feature_request - Get single feature request
- POST /api/method/feature_tracker.api.feature_requests.create_feature_request - Create new feature request
- PUT /api/method/feature_tracker.api.feature_requests.update_feature_request - Update existing feature request
- DELETE /api/method/feature_tracker.api.feature_requests.delete_feature_request - Delete feature request
- GET /api/method/feature_tracker.api.feature_requests.get_feature_request_stats - Get statistics
"""

import frappe, feature_tracker
from frappe import _
from frappe.utils import cint, today, getdate, add_days
from typing import Dict, Optional, Any
import json


# Constants for validation
VALID_PRIORITIES = ["High", "Medium", "Low"]
VALID_STATUSES = ["Opened", "Pending", "In Progress", "Approved", "Rejected", "Closed", "Canceled"]
DEFAULT_FIELDS = ['name', 'title', 'description', 'status', 'priority', 'date', 'creation', 'modified', 'owner', 'modified_by']
MAX_PAGE_LENGTH = 100


def _validate_permission(permission_type: str, doc_name: Optional[str] = None) -> None:
    """Validate user permissions for Feature Request doctype"""
    if not frappe.has_permission("Feature Request", permission_type, doc_name):
        frappe.throw(_(feature_tracker.ERRORS.get("no_read_permission")), frappe.PermissionError)


def _validate_document_exists(name: str) -> None:
    """Validate that a Feature Request document exists"""
    if not frappe.db.exists("Feature Request", name):
        frappe.throw(_(feature_tracker.ERRORS.get("feature_request_not_exist")).format(name), frappe.DoesNotExistError)


def _validate_required_field(value: str, field_name: str) -> None:
    """Validate that a required field is not empty"""
    if not value or not value.strip():
        frappe.throw(_(feature_tracker.ERRORS.get("field_required")).format(field_name), frappe.ValidationError)


def _validate_choice_field(value: str, field_name: str, valid_choices: list) -> None:
    """Validate that a field value is from the allowed choices"""
    if value not in valid_choices:
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_choice")).format(field_name, ", ".join(valid_choices)), frappe.ValidationError)


def _validate_date_format(date_str: str) -> None:
    """Validate date format"""
    try:
        getdate(date_str)
    except Exception:
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_date_format")), frappe.ValidationError)


def _parse_filters(filters: Optional[str]) -> Dict:
    """Parse and validate filters parameter"""
    if not filters:
        return {}
    
    try:
        return json.loads(filters) if isinstance(filters, str) else filters
    except (json.JSONDecodeError, TypeError):
        frappe.throw(_(feature_tracker.ERRORS.get("invalid_filters_format")), frappe.ValidationError)


def _build_search_filters(search: str, existing_filters: Dict) -> Dict:
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


def _get_pagination_info(total_count: int, limit_start: int, limit_page_length: int) -> Dict:
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


@frappe.whitelist()
def get_feature_requests(
    filters: Optional[str] = None,
    fields: Optional[str] = None,
    order_by: Optional[str] = None,
    limit_start: int = 0,
    limit_page_length: int = 20,
    search: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get list of feature requests with filtering, pagination, and search capabilities.
    """
    try:
        # Validate permissions
        _validate_permission("read")
        
        # Parse and validate parameters
        parsed_filters = _parse_filters(filters)
        field_list = [field.strip() for field in fields.split(',')] if fields else DEFAULT_FIELDS
        order_by = order_by or 'creation desc'
        limit_start = cint(limit_start)
        limit_page_length = min(cint(limit_page_length), MAX_PAGE_LENGTH)
        
        # Add search filters if provided
        if search:
            parsed_filters = _build_search_filters(search, parsed_filters)
        
        # Get data
        total_count = frappe.db.count('Feature Request', filters=parsed_filters)
        data = frappe.get_all(
            'Feature Request',
            filters=parsed_filters,
            fields=field_list,
            order_by=order_by,
            limit_start=limit_start,
            limit_page_length=limit_page_length
        )
        
        return {
            'data': data,
            'total_count': total_count,
            'page_info': _get_pagination_info(total_count, limit_start, limit_page_length)
        }
        
    except Exception as e:
        frappe.log_error(f"Error in get_feature_requests: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_fetching_feature_requests")), frappe.ValidationError)


@frappe.whitelist()
def get_feature_request(name: str) -> Dict[str, Any]:
    """
    Get a single feature request by name.
    """
    try:
        # Validate input and permissions
        _validate_required_field(name, "Feature Request name")
        _validate_document_exists(name)
        _validate_permission("read", name)
        
        # Get document
        doc = frappe.get_doc("Feature Request", name)
        
        return {
            'name': doc.name,
            'title': doc.title,
            'description': doc.description,
            'status': doc.status,
            'priority': doc.priority,
            'date': doc.date,
            'creation': doc.creation,
            'modified': doc.modified,
            'owner': doc.owner,
            'modified_by': doc.modified_by,
            'docstatus': doc.docstatus
        }
        
    except Exception as e:
        frappe.log_error(f"Error in get_feature_request: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_fetching_feature_request")), frappe.ValidationError)


@frappe.whitelist()
def create_feature_request(
    title: str,
    description: str,
    priority: str = "Medium",
    status: str = "Opened",
    date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new feature request.
    """
    try:
        # Validate permissions
        _validate_permission("create")
        
        # Validate required fields
        _validate_required_field(title, "Title")
        _validate_required_field(description, "Description")
        
        # Validate choice fields
        _validate_choice_field(priority, "Priority", VALID_PRIORITIES)
        _validate_choice_field(status, "Status", VALID_STATUSES)
        
        # Validate and set date
        if date:
            _validate_date_format(date)
        else:
            date = today()
        
        # Create document
        doc = frappe.get_doc({
            "doctype": "Feature Request",
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "status": status,
            "date": date
        })
        
        doc.insert()
        frappe.db.commit()
        
        return {
            'name': doc.name,
            'title': doc.title,
            'description': doc.description,
            'status': doc.status,
            'priority': doc.priority,
            'date': doc.date,
            'creation': doc.creation,
            'modified': doc.modified,
            'owner': doc.owner,
            'modified_by': doc.modified_by,
            'docstatus': doc.docstatus,
            'message': _("Feature Request created successfully")
        }
        
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(f"Error in create_feature_request: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_creating_feature_request")), frappe.ValidationError)


@frappe.whitelist()
def update_feature_request(
    name: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    priority: Optional[str] = None,
    status: Optional[str] = None,
    date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing feature request.
    """
    try:
        # Validate input and permissions
        _validate_required_field(name, "Feature Request name")
        _validate_document_exists(name)
        _validate_permission("write", name)
        
        # Get document
        doc = frappe.get_doc("Feature Request", name)
        
        # Update fields if provided
        if title is not None:
            _validate_required_field(title, "Title")
            doc.title = title.strip()
            
        if description is not None:
            _validate_required_field(description, "Description")
            doc.description = description.strip()
            
        if priority is not None:
            _validate_choice_field(priority, "Priority", VALID_PRIORITIES)
            doc.priority = priority
            
        if status is not None:
            _validate_choice_field(status, "Status", VALID_STATUSES)
            doc.status = status
            
        if date is not None:
            _validate_date_format(date)
            doc.date = date
        
        # Save document
        doc.save()
        frappe.db.commit()
        
        return {
            'name': doc.name,
            'title': doc.title,
            'description': doc.description,
            'status': doc.status,
            'priority': doc.priority,
            'date': doc.date,
            'creation': doc.creation,
            'modified': doc.modified,
            'owner': doc.owner,
            'modified_by': doc.modified_by,
            'docstatus': doc.docstatus,
            'message': _("Feature Request updated successfully")
        }
        
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(f"Error in update_feature_request: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_updating_feature_request")), frappe.ValidationError)


@frappe.whitelist()
def delete_feature_request(name: str) -> Dict[str, Any]:
    """
    Delete a feature request.
    """
    try:
        # Validate input and permissions
        _validate_required_field(name, "Feature Request name")
        _validate_document_exists(name)
        _validate_permission("delete", name)
        
        # Get document for logging
        doc = frappe.get_doc("Feature Request", name)
        title = doc.title
        
        # Delete document
        frappe.delete_doc("Feature Request", name)
        frappe.db.commit()
        
        return {
            'name': name,
            'title': title,
            'message': _("Feature Request '{0}' deleted successfully").format(title)
        }
        
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(f"Error in delete_feature_request: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_deleting_feature_request")), frappe.ValidationError)


@frappe.whitelist()
def get_feature_request_stats() -> Dict[str, Any]:
    """
    Get statistics about feature requests.
    """
    try:
        # Validate permissions
        _validate_permission("read")
        
        # Get status counts
        status_counts = frappe.db.sql("""
            SELECT status, COUNT(*) as count
            FROM `tabFeature Request`
            GROUP BY status
            ORDER BY count DESC
        """, as_dict=True)
        
        # Get priority counts
        priority_counts = frappe.db.sql("""
            SELECT priority, COUNT(*) as count
            FROM `tabFeature Request`
            GROUP BY priority
            ORDER BY FIELD(priority, 'High', 'Medium', 'Low')
        """, as_dict=True)
        
        # Get total and recent counts
        total_count = frappe.db.count("Feature Request")
        recent_date = add_days(today(), -7)
        recent_count = frappe.db.count("Feature Request", {"creation": [">=", recent_date]})
        
        return {
            'total_count': total_count,
            'recent_count': recent_count,
            'status_breakdown': status_counts,
            'priority_breakdown': priority_counts
        }
        
    except Exception as e:
        frappe.log_error(f"Error in get_feature_request_stats: {str(e)}")
        frappe.throw(_(feature_tracker.ERRORS.get("error_fetching_statistics")), frappe.ValidationError)