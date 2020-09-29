from flask import Flask, request, jsonify, json, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class About(Resource):
    def get(self):
        return jsonify({'about': 'send a get request with numbers num1 and num2 to /add or /sub'})

class Hi(Resource):
    def get(self):
        return jsonify({'message': "Hello"})


class Sum(Resource):
    def post(self):
        num_json= request.get_json()
        num_json= request.json
        num1 = num_json.get('num1')
        num2 = num_json.get('num2')
        message = json.dumps({'sum': num1+num2})
        return Response(message, status=201, mimetype='application/json')

class Sub(Resource):
    def post(self):
        num_json= request.get_json()
        num_json= request.json
        num1 = num_json.get('num1')
        num2 = num_json.get('num2')
        message = json.dumps({'dif': num1-num2})
        return Response(message, status=201, mimetype='application/json')

class Mult(Resource):
    def post(self):
        num_json= request.get_json()
        num_json= request.json
        num1 = num_json.get('num1')
        num2 = num_json.get('num2')
        message = json.dumps({'prod': num1*num2})
        return Response(message, status=201, mimetype='application/json')

class Div(Resource):
    def post(self):
        num_json= request.get_json()
        num_json= request.json
        num1 = num_json.get('num1')
        num2 = num_json.get('num2')
        message = json.dumps({'quo': num1/num2})
        return Response(message, status=201, mimetype='application/json')

api.add_resource(About, '/')
api.add_resource(Hi, '/hi')
api.add_resource(Sum, '/sum')
api.add_resource(Sub, '/sub')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

