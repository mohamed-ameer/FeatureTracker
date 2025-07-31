from setuptools import setup, find_packages

# get version from __version__ variable in feature_tracker/__init__.py
from feature_tracker import __version__ as version

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="feature_tracker",
	version=version,
	description="An internal feature tracking tool built with Frappe, designed to help teams monitor the development progress of product features.",
	author="Mohamed Amir",
	author_email="mohamedamirr424@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
