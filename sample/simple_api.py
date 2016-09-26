import falcon
import json
 
class QuoteResource:
    def on_post(self, req, resp):
    	quote= {}
    	print(req.get_param('sessionKey'))
    	quote['data']=req.get_param('sessionKey')
        resp.body = json.dumps(quote)
 
api = falcon.API()
api.add_route('/quote', QuoteResource())