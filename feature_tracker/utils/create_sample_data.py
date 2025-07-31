import frappe
from frappe.utils import today, add_days

def create_sample_feature_requests():
    """Create sample feature requests for testing the roadmap"""
    
    sample_features = [
        {
            "title": "Ability to create ad hoc task in leader dashboard",
            "description": "Allow leaders to create ad hoc tasks directly from their dashboard without going through the full task creation process.",
            "status": "Opened",
            "priority": "High",
            "date": today()
        },
        {
            "title": "Enhanced user authentication system",
            "description": "Implement two-factor authentication and improved password policies for better security.",
            "status": "In Progress",
            "priority": "High",
            "date": add_days(today(), -5)
        },
        {
            "title": "Mobile responsive design improvements",
            "description": "Optimize the application for mobile devices with better responsive design patterns.",
            "status": "Pending",
            "priority": "Medium",
            "date": add_days(today(), -2)
        },
        {
            "title": "Advanced reporting dashboard",
            "description": "Create comprehensive reporting dashboard with charts and analytics for better insights.",
            "status": "Approved",
            "priority": "Medium",
            "date": add_days(today(), -10)
        },
        {
            "title": "Email notification system",
            "description": "Implement automated email notifications for important events and updates.",
            "status": "Closed",
            "priority": "Low",
            "date": add_days(today(), -15)
        },
        {
            "title": "Dark mode theme support",
            "description": "Add dark mode theme option for better user experience in low-light environments.",
            "status": "Opened",
            "priority": "Low",
            "date": add_days(today(), -1)
        },
        {
            "title": "API rate limiting and throttling",
            "description": "Implement rate limiting to prevent API abuse and ensure fair usage.",
            "status": "In Progress",
            "priority": "High",
            "date": add_days(today(), -7)
        },
        {
            "title": "Bulk data import/export functionality",
            "description": "Allow users to import and export large datasets in various formats (CSV, Excel, JSON).",
            "status": "Pending",
            "priority": "Medium",
            "date": add_days(today(), -3)
        }
    ]
    
    created_count = 0
    
    for feature_data in sample_features:
        # Check if a feature with this title already exists
        existing = frappe.db.exists("Feature Request", {"title": feature_data["title"]})
        
        if not existing:
            try:
                feature = frappe.get_doc({
                    "doctype": "Feature Request",
                    "title": feature_data["title"],
                    "description": feature_data["description"],
                    "status": feature_data["status"],
                    "priority": feature_data["priority"],
                    "date": feature_data["date"]
                })
                
                feature.insert(ignore_permissions=True)
                created_count += 1
                print(f"Created feature request: {feature_data['title']}")
                
            except Exception as e:
                print(f"Error creating feature request '{feature_data['title']}': {str(e)}")
        else:
            print(f"Feature request already exists: {feature_data['title']}")
    
    frappe.db.commit()
    print(f"\nSample data creation completed. Created {created_count} new feature requests.")
    
    return created_count

if __name__ == "__main__":
    create_sample_feature_requests()
