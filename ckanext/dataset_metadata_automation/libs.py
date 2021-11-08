# encoding: utf-8

import ckan.plugins.toolkit as toolkit

class Helper():

    def get_user_name():

        return toolkit.g.userobj.fullname
    
    def get_user_email():

        return toolkit.g.userobj.email