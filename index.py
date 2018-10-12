# social cops task for backend internship

# Task is available here
# https://docs.google.com/document/d/11rzhE7oTKZNnqvK6b_AOo9QmquK7hPxoQfup72r3DLY/edit

# importing flask class from flask package
import os
import sys
import requests
from flask import jsonify, request, make_response, send_from_directory

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))


import logger
from app import app


#logger object to log the info and debug
LOG = logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))

# port
PORT = os.environ.get('PORT')


@app.errorhandler(404)
def error_404(error):
    LOG.error(error)
    return make_response(jsonify({'error':'Page not found'}), 404)


# routes for main page
@app.route('/')

# view for main page
def index():
    return send_from_directory('dist', 'index.html')

# starting the server
if __name__ == "__main__":
    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development'
    app.run(host='0.0.0.0', port=int(PORT))
