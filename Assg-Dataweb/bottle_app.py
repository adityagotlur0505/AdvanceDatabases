
# very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello from ADITYA Gotlur(811229613)!'
=======
    return 'Hello from Aditya Gotlur!'
>>>>>>> 7551ba7349628431c6f743d1a524ab98016dceda

application = default_app()
