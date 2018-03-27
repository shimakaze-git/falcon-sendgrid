# coding=utf-8
import sendgrid
import falcon

from falcon_sendgrid import SendGridManagement

class SendGridResource(object):
    _manager = None
    
    def __init__(self):
        self._manager = SendGridManagement()
        
        #check apikey
        self.confirm_api_key()

    def confirm_api_key(self):
        """
        Confirm existence of APIkey
        """
        
        if self._manager._api_key == None:
            raise falcon.HTTPBadRequest('None API_KEY')