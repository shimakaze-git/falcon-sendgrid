# coding=utf-8

import falcon
import sendgrid
import json
import time

from .sendgrid import SendGridResource
from .hooks import JSONTranslator

from sendgrid.helpers.mail import *

@falcon.before(JSONTranslator().before_resource)
@falcon.after(JSONTranslator().after_resource)
class SendMailResource(SendGridResource):
    
    def __init__(self):
        super().__init__()
        
    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):

        data = req.context['data']
        
        # check data
        if self.check_data(data) != True:
            raise falcon.HTTPBadRequest('lacking request body')

        from_email = Email(data['from'])
        to_email = Email(data['to'])
        subject = data['subject']
        content = Content("text/plain", data['content'])
        mail = Mail(from_email, subject, to_email, content)
        
        try:
            response = self.mail_send_post(mail.get())
        except:
            raise falcon.HTTPError(falcon.HTTP_753, 'failed send email')
        
        # resp.body = '{"message": "Hello world!"}'
        # resp.status = falcon.HTTP_200

        # response.headers
        resp.body = response.body
        resp.status = response.status_code
        
    def check_data(self, data):
        """
        check data
        """

        check_dictionary = {
            'from',
            'to',
            'subject',
            'content',
        }
        
        if set(data) >= check_dictionary:
            return True
        else:
            return False
    
    def mail_send_post(self, request_body):
        """
        mail send process
        """
        sg = self._manager._sg
        response = sg.client.mail.send.post(request_body=request_body)

        return response