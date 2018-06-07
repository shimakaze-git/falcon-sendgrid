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

        """ set Email. """
        mail = self.set_email(data)
        
        try:
            response = self.mail_send_post(mail.get())
        except:
            raise falcon.HTTPError(falcon.HTTP_753, 'failed send email')

        # response.headers
        if (300 > response.status_code) and (response.status_code >= 200):
            # resp.body = json.dumps({
            #     'status': 1,
            #     'message': response.body
            # })
            resp.body = '{"status": 1 ,"message": "' + response.body + '"}'
            resp.status = falcon.HTTP_200

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
        
    def set_email(self, data):
        """
        set Email data
        """
        if self._manager._from_email_address != None:
            from_email_address = self._manager._from_email_address
        else:
            from_email_address = data['from']
        
        from_email = Email(from_email_address)
        to_email = Email(data['to'])
        subject = data['subject']
        content = Content("text/plain", data['content'])
        mail = Mail(
            from_email,
            subject,
            to_email,
            content
        )
        
        return mail