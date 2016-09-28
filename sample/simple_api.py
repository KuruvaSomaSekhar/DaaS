import falcon
import json
import logging

logging.basicConfig(filename='/ws.log',level=logging.DEBUG)
 
class QuoteResource:
    def on_post(self, req, resp):
    	quote= {}
    	logging.info(req.options)
    	logging.info(type(req.options))
    	logging.info(req.params)
    	logging.info(req.headers)
    	logging.info(req.path)
    	logging.info(req.get_param('data'))
    	quote['data']=req.get_param('data')
    	logging.info(json.dumps(quote))
        resp.body = json.dumps(quote)
 
api = falcon.API()
api.add_route('/quote', QuoteResource())