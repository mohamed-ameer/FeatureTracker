# Feature Tracker Constants

# App Information
APP_NAME = "Feature Tracker"
APP_VERSION = "0.0.1"

# Error Messages
ERRORS = {
    # Permission Errors
    "no_read_permission": "Not permitted to read Feature Request",
    "no_create_permission": "Not permitted to create Feature Request",
    "no_update_permission": "Not permitted to update Feature Request {0}",
    "no_delete_permission": "Not permitted to delete Feature Request {0}",

    # Validation Errors
    "invalid_filters_format": "Invalid filters format",
    "feature_request_name_required": "Feature Request name is required",
    "feature_request_not_exist": "Feature Request {0} does not exist",
    "title_required": "Title is required",
    "description_required": "Description is required",
    "title_cannot_be_empty": "Title cannot be empty",
    "description_cannot_be_empty": "Description cannot be empty",
    "invalid_priority": "Priority must be one of: {0}",
    "invalid_status": "Status must be one of: {0}",
    "invalid_date_format": "Invalid date format. Use YYYY-MM-DD",

    # Generic Errors
    "error_fetching_feature_requests": "An error occurred while fetching feature requests",
    "error_fetching_feature_request": "An error occurred while fetching the feature request",
    "error_creating_feature_request": "An error occurred while creating the feature request",
    "error_updating_feature_request": "An error occurred while updating the feature request",
    "error_deleting_feature_request": "An error occurred while deleting the feature request",
    "error_fetching_statistics": "An error occurred while fetching statistics",
}