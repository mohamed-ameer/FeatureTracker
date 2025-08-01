# Feature Tracker App By Mohamed Amir

[Screencast from 08-01-2025 02:19:02 AM.webm](https://github.com/user-attachments/assets/01bc7a42-35fb-440c-b7e8-b9d50632dbbe)


## Overview

An internal feature tracking tool built with Frappe, designed to help teams monitor the development progress of product features.

## Disclaimer

Installing or Updating this app may result in data overwriting or data loss regarding the following modules:

1. Workspaces

### Installation

1. Install the App to the bench from the Repository:

```
bench get-app https://github.com/mohamed-ameer/FeatureTracker.git
```

2. Install the App to the site:

```
bench --site [site-name] install-app feature_tracker
```

3. Migrate the changes:

```
bench --site [site-name] migrate
```

4. Build the App:

```
bench --site [site-name] build
```

## Updating the App

1. Update the App

```
bench update --reset --apps feature_tracker
```

2. Migrate the changes:

```
bench --site [site-name] migrate
```

3. Build the App:

```
bench --site [site-name] build
```

## Uninstalling the App

1. Uninstall the App from the site:

```
bench --site [site-name] uninstall-app feature_tracker
```

2. Remove the App from the bench:

```
bench remove-app feature_tracker
```
