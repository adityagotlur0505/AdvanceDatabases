
# very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from ADITYA Gotlur(811229613)!'

application = default_app()
