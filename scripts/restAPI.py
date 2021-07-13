# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Resource, Api
from converter import converter

# Flask- , FlaskRESTFUL application object
app = Flask(__name__)
api = Api(app)

# flask renders by default ascii
api.app.config.update(
    JSON_AS_ASCII = False,
    JSONIFY_PRETTYPRINT_REGULAR = True
)

class OperationsCenter(Resource):
    def get(self, rlcode):
        operationsCenter = converter(rlcode)
        return jsonify(operationsCenter)

api.add_resource(OperationsCenter, '/betriebsstelle/<rlcode>')

if __name__ == '__main__':
    app.run(debug=True, port='8080', host='127.0.0.1')