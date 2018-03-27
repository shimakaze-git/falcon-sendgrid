# coding=utf-8

import falcon
import sendgrid
import json

from .sendgrid import SendGridResource
from sendgrid.helpers import mail

class SendMailResource(SendGridResource):
    
    def __init__(self):
        super().__init__()
        
    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200
        
    def on_post(self, req, resp):
        
        body = req.stream.read()
        data = json.loads(body.decode('utf-8'))

        api_key = self._manager._api_key
        
        # from_email = mail.Email("test@example.com")
        # to_email = mail.Email("test@example.com")
        # subject = "Sending with SendGrid is Fun"
        # content = mail.Content("text/plain", "and easy to do anywhere, even with Python")
        # mail = mail.Mail(from_email, subject, to_email, content)

        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200
    