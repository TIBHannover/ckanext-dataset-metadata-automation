[![CI](https://github.com/TIBHannover/ckanext-dataset-metadata-automation/actions/workflows/test.yml/badge.svg)](https://github.com/TIBHannover/ckanext-dataset-metadata-automation/actions/workflows/test.yml)


# ckanext-dataset-metadata-automation

The CKAN plugin for pre-filling some of the dataset metadata for a user.

- author name and email
 - maintainer name and email


## Requirements



Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.9  | Yes    |
| earlier       | not tested    |


## Installation

To install ckanext-dataset-metadata-automation:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

        git clone https://github.com//ckanext-dataset-metadata-automation.git
        cd ckanext-dataset-metadata-automation
        pip install -e .
        pip install -r requirements.txt
        python setup.py develop

3. Add `dataset_metadata_automation` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

         sudo service apache2 reload


