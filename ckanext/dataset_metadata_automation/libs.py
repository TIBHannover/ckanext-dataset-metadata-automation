# encoding: utf-8

import ckan.plugins.toolkit as toolkit

class Helper():

    def get_user_name():
        user = getattr(toolkit.g, 'userobj', None)
        return user.fullname if user else ''
    
    def get_user_email():
        user = getattr(toolkit.g, 'userobj', None)
        return user.email if user else ''
