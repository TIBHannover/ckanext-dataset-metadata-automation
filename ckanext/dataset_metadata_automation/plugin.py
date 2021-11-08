import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.dataset_metadata_automation.libs import Helper


class DatasetMetadataAutomationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        

    def get_helpers(self):

        return {'get_user_name': Helper.get_user_name,
            'get_user_email': Helper.get_user_email}