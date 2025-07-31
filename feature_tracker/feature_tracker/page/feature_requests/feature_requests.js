frappe.pages['feature-requests'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Feature Requests Roadmap',
		single_column: true
	});

	// Add custom CSS for roadmap
	frappe.require('/assets/feature_tracker/css/roadmap-page.css');

	// Initialize the roadmap
	new FeatureRequestsRoadmap(page);
}

class FeatureRequestsRoadmap {
	constructor(page) {
		this.page = page;
		this.features = [];
		this.init();
	}

	init() {
		this.setup_page();
		this.load_features();
	}

	setup_page() {
		// Add primary action button
		this.page.set_primary_action('New Feature Request', () => {
			frappe.new_doc('Feature Request');
		}, 'add');
		// Add back button to the list view
		this.page.set_secondary_action('Back to Feature Requests List', () => {
			frappe.set_route('List', 'Feature Request');
		});

		// Create the roadmap HTML structure
		this.page.main.html(`
			<div class="roadmap-container">
				<div class="roadmap-header">
					<h2>Roadmap</h2>
					<p class="text-muted">Last synced ${frappe.datetime.comment_when(frappe.datetime.now_datetime())}</p>
				</div>

				<div class="roadmap-board row">
					<div class="col-md-4">
						<div class="roadmap-column" data-status="planned">
							<div class="column-header">
								<h4>Planned <span class="badge badge-light feature-count" id="planned-count">0</span></h4>
								<p class="text-muted small">Features to be developed</p>
							</div>
							<div class="feature-cards" id="planned-cards">
								<!-- Feature cards will be populated here -->
							</div>
						</div>
					</div>

					<div class="col-md-4">
						<div class="roadmap-column" data-status="in-progress">
							<div class="column-header">
								<h4>In Progress <span class="badge badge-light feature-count" id="progress-count">0</span></h4>
								<p class="text-muted small">Currently being developed</p>
							</div>
							<div class="feature-cards" id="progress-cards">
								<!-- Feature cards will be populated here -->
							</div>
						</div>
					</div>

					<div class="col-md-4">
						<div class="roadmap-column" data-status="complete">
							<div class="column-header">
								<h4>Complete <span class="badge badge-light feature-count" id="complete-count">0</span></h4>
								<p class="text-muted small">Completed features</p>
							</div>
							<div class="feature-cards" id="complete-cards">
								<!-- Feature cards will be populated here -->
							</div>
						</div>
					</div>
				</div>
			</div>
		`);
	}

	async load_features() {
		try {
			// Show loading state
			this.show_loading();

			// Fetch features using Frappe's call method
			const response = await frappe.call({
				method: 'frappe.client.get_list',
				args: {
					doctype: 'Feature Request',
					fields: ['name', 'title', 'description', 'status', 'priority', 'date'],
					limit_page_length: 100,
					order_by: 'creation desc'
				}
			});

			this.features = response.message || [];
			this.render_features();
			this.update_counts();
		} catch (error) {
			console.error('Error loading features:', error);
			frappe.msgprint({
				title: 'Error',
				message: 'Failed to load feature requests. Please try again.',
				indicator: 'red'
			});
		}
	}

	show_loading() {
		const columns = ['planned-cards', 'progress-cards', 'complete-cards'];
		columns.forEach(columnId => {
			const container = this.page.main.find(`#${columnId}`);
			container.html('<div class="text-center text-muted p-4">Loading...</div>');
		});
	}

	render_features() {
		// Clear existing cards
		this.page.main.find('#planned-cards').empty();
		this.page.main.find('#progress-cards').empty();
		this.page.main.find('#complete-cards').empty();

		// Group features by status
		const groupedFeatures = this.group_features_by_status();

		// Render each group
		Object.keys(groupedFeatures).forEach(status => {
			const containerId = this.get_container_id_for_status(status);
			const container = this.page.main.find(`#${containerId}`);

			groupedFeatures[status].forEach((feature, index) => {
				const card = this.create_feature_card(feature, index + 1);
				container.append(card);
			});

			// Show empty state if no features
			if (groupedFeatures[status].length === 0) {
				container.html('<div class="text-center text-muted p-4">No features</div>');
			}
		});
	}

	group_features_by_status() {
		const groups = {
			planned: [],
			'in-progress': [],
			complete: []
		};

		this.features.forEach(feature => {
			const status = feature.status.toLowerCase();

			if (status === 'opened' || status === 'pending') {
				groups.planned.push(feature);
			} else if (status === 'in progress') {
				groups['in-progress'].push(feature);
			} else if (status === 'approved' || status === 'closed') {
				groups.complete.push(feature);
			}
		});

		return groups;
	}

	get_container_id_for_status(status) {
		const mapping = {
			'planned': 'planned-cards',
			'in-progress': 'progress-cards',
			'complete': 'complete-cards'
		};
		return mapping[status] || 'planned-cards';
	}

	create_feature_card(feature, number) {
		const priorityClass = `priority-${feature.priority.toLowerCase()}`;
		const formattedDate = frappe.datetime.str_to_user(feature.date);

		const card = $(`
			<div class="feature-card card mb-3" data-feature-name="${feature.name}">
				<div class="card-body">
					<div class="feature-card-header d-flex align-items-start mb-2">
						<div class="feature-icon bg-warning text-dark rounded mr-2 d-flex align-items-center justify-content-center"
							 style="width: 24px; height: 24px; font-size: 12px; font-weight: bold;">
							⚠
						</div>
						<div class="feature-number text-muted small">${number.toString().padStart(3, '0')}</div>
					</div>
					<h6 class="feature-title card-title">${frappe.utils.escape_html(feature.title)}</h6>
					<div class="feature-meta d-flex justify-content-between align-items-center mt-2">
						<span class="badge badge-${this.get_priority_color(feature.priority)} ${priorityClass}">${feature.priority}</span>
						<small class="text-muted">${formattedDate}</small>
					</div>
				</div>
			</div>
		`);

		// Add click event to show details
		card.on('click', () => {
			this.show_feature_details(feature);
		});

		return card;
	}

	get_priority_color(priority) {
		const colors = {
			'High': 'danger',
			'Medium': 'warning',
			'Low': 'success'
		};
		return colors[priority] || 'secondary';
	}

	update_counts() {
		const groups = this.group_features_by_status();

		this.page.main.find('#planned-count').text(groups.planned.length);
		this.page.main.find('#progress-count').text(groups['in-progress'].length);
		this.page.main.find('#complete-count').text(groups.complete.length);
	}

	show_feature_details(feature) {
		// Create a dialog to show feature details
		const dialog = new frappe.ui.Dialog({
			title: 'Feature Request Details',
			fields: [
				{
					fieldtype: 'Data',
					fieldname: 'title',
					label: 'Title',
					read_only: 1,
					default: feature.title
				},
				{
					fieldtype: 'Select',
					fieldname: 'status',
					label: 'Status',
					read_only: 1,
					default: feature.status
				},
				{
					fieldtype: 'Select',
					fieldname: 'priority',
					label: 'Priority',
					read_only: 1,
					default: feature.priority
				},
				{
					fieldtype: 'Date',
					fieldname: 'date',
					label: 'Date',
					read_only: 1,
					default: feature.date
				},
				{
					fieldtype: 'Long Text',
					fieldname: 'description',
					label: 'Description',
					read_only: 1,
					default: feature.description || 'No description provided.'
				}
			],
			primary_action_label: 'Edit',
			primary_action: () => {
				frappe.set_route('Form', 'Feature Request', feature.name);
				dialog.hide();
			},
			secondary_action_label: 'Delete',
			secondary_action: () => {
				this.delete_feature(feature, dialog);
			}
		});

		dialog.show();
	}

	delete_feature(feature, dialog) {
		frappe.confirm(
			`Are you sure you want to delete the feature request "${feature.title}"?`,
			() => {
				frappe.call({
					method: 'frappe.client.delete',
					args: {
						doctype: 'Feature Request',
						name: feature.name
					},
					callback: (response) => {
						if (!response.exc) {
							frappe.show_alert({
								message: 'Feature request deleted successfully',
								indicator: 'green'
							});
							dialog.hide();
							this.load_features(); // Reload features
						}
					}
				});
			}
		);
	}
}