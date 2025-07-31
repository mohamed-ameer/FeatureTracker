frappe.listview_settings['Feature Request'] = {
    onload(listview) {
        listview.page.add_button(__('Go To Feature Requests Page'), () => {
            frappe.set_route('/feature-requests');
        });
    }
}