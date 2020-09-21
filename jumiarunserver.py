"""
This script runs the HydraWeb application using a development server.
"""

from os import environ
from jumiaApi import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '127.0.0.1')
    try:
        PORT = int(environ.get('SERVER_PORT', '5400'))
    except ValueError:
        PORT = 5400
    app.run(HOST, PORT)
    #app.run(host='68.66.205.156', port=5400, debug=True)
