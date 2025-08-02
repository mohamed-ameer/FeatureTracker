# Feature Tracker App By Mohamed Amir

https://github.com/user-attachments/assets/a597961d-4a6f-48b5-b60a-a1e7d1adb3dc

#### [see in production: http://147.182.198.64/](http://147.182.198.64/)

- username: Administrator
- password: admin

---

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
---

## Installing using Docker

[![View on Docker Hub](https://img.shields.io/badge/Docker%20Hub-View%20on%20Docker%20Hub-2496ED?style=for-the-badge&logo=docker)](https://hub.docker.com/r/ameer577/feature_tracker)

1. Pull the image from dockerhub:

```
docker pull ameer577/feature_tracker:latest
```

2. Clone frappe_docker

```
git clone https://github.com/frappe/frappe_docker 
cd frappe_docker
```

3. Setup the image in the `pwd.yml` file:

```
nano pwd.yml
```

change any `frappe/erpnext:v15.60.1` with your image (eg. `ameer577/feature_tracker:latest` )

then,

replace `--install-app erpnext` with `--install-app erpnext --install-app feature_tracker` 

4. Start the container using docker compose

```bash
docker compose -f pwd.yml up -d
docker logs frappe_container-create-site-1 -f
```
