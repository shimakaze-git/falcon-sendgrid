# coding=utf-8
import sendgrid

class SendGridManagement(object):
    _api_key = ""
    _sg = None
    
    def __init__(self):
        print('SnedGridManagement')
        print(self)
        
    @classmethod
    def set_apikey(cls, api_key):
        cls._api_key = api_key
        cls._sg = sendgrid.SendGridAPIClient(api_key=cls._api_key)

        print(cls)
        print('set_apikey : %s' % (api_key))
        print('cls.api_key: %s' % (cls._api_key))
        