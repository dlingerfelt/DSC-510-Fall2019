from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
class HelloWorld(Resource):

    def get(self):
        ret_value =  """
        '<!doctype html>
    <html Lang="en">

    <head>
    <meta charset="utf-8">
    <title>Learning about HTML</title>
    </head>
    <h1>
    Creating web pages with HTML
    </h1>
    <p>
    Building a web page is a step towards building great web pages.
    </p>
    <ul HTML Elements>
    <li>Head</li>
    <li>H1 for header1</li>
    <li>P for paragraph</li>
    </ul>
    </html>'
    """
        return {'ret_value'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(port=5001)
