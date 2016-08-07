"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask_restful import Resource, Api

from flask import Flask, send_from_directory

app = Flask(__name__)
api = Api(app)


class Main(Resource):
	@staticmethod
	def get():
		return send_from_directory('templates', 'index.html')


@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500


@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500

from handlers import root, prs
