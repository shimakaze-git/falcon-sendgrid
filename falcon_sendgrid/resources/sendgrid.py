# coding=utf-8
import sendgrid

from falcon_sendgrid import SendGridManagement

class SendGridResource(object):
    _manager = None
    
    def __init__(self):
        self._manager = SendGridManagement()
        
        print('self._manager = SendGridManagement()')
        print(self._manager)