# coding=utf-8
import sendgrid

class SendGridManagement(object):
    _api_key = None
    _sg = None
    
    _from_email_address = None
    
    def __init__(self):
        pass
        
    @classmethod
    def set_apikey(cls, api_key):
        cls._api_key = api_key
        cls._sg = sendgrid.SendGridAPIClient(api_key=cls._api_key)

    @classmethod
    def set_fromemail(cls, address):
        cls._from_email_address = address