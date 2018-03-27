# coding=utf-8
import json
import falcon

class JSONTranslator(object):
    
    def before_resource(self, req, resp, resource, params):

        # RequestHeader check
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.')
        
        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.')
        
        if req.content_length in (None, 0):
            # Nothing to do
            return

        # convert to json
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body')
        
        try:
            req.context['data'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON')

    def after_resource(self, req, resp, resource):
        pass
