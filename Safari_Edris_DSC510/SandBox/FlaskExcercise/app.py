from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    #return '<!doctype html><html><head></head><body>Hello There!</body></html>'
    return """
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


if __name__ == '__main__':
    app.run()
