# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased] - YYYY-MM-DD

### Added

- Add comprehensive CRUD API for Feature Request doctype
	- `GET /api/method/feature_tracker.api.feature_requests.get_feature_requests` - List feature requests with pagination, filtering, and search
	- `GET /api/method/feature_tracker.api.feature_requests.get_feature_request` - Get single feature request by name
	- `POST /api/method/feature_tracker.api.feature_requests.create_feature_request` - Create new feature request
	- `PUT /api/method/feature_tracker.api.feature_requests.update_feature_request` - Update existing feature request
	- `DELETE /api/method/feature_tracker.api.feature_requests.delete_feature_request` - Delete feature request
	- `GET /api/method/feature_tracker.api.feature_requests.get_feature_request_stats` - Get statistics and analytics
	- `POST /api/method/feature_tracker.api.feature_requests.bulk_update_status` - Bulk update status for multiple requests
- Add custom roadmap page for Feature Requests at `/app/feature-requests`
	- Three-column layout: Planned, In Progress, Complete
	- Interactive feature cards with click-to-view details
	- Modal dialogs for feature request details with edit/delete actions
	- Real-time count updates for each status column
	- Professional styling with hover effects and animations
	- Responsive design for desktop, tablet, and mobile devices
- Add centralized error message constants in `constants.py`
	- standardized error message constants for consistent error handling
	- Permission errors, validation errors, and generic error messages
- Add Arabic translations for all error messages in `translations/ar.csv`
	- Complete Arabic translation support for all API error messages, WorkSpace UI and Feature Request doctype
- Add Postman collection for comprehensive API testing
	- 13 test scenarios covering all CRUD operations
	- Authentication examples (session-based and API key)
	- Environment variables for easy setup
- Add shortcuts for roadmap page access and feature request creation
