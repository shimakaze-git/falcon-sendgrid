# coding=utf-8

import falcon

from falcon_sendgrid import SendGridManagement
from falcon_sendgrid.resources.sendmail import SendMailResource

config = {
    "API_KEY" : 'abcdefghijklmnopqrstuvwxyz0123456789'
}
SendGridManagement().set_apikey(config['API_KEY'])

app = falcon.API()
app.add_route('/sendmail', SendMailResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()