from flask import make_response, render_template

from flask_restful import Resource
from main import api


class Home(Resource):
	@staticmethod
	def get():
		return make_response(render_template('home.html'))


class Dashboard(Resource):
	@staticmethod
	def get():
		return make_response(render_template('dashboard.html'))


class User(Resource):
	@staticmethod
	def get():
		return make_response(render_template('user.html'))


api.add_resource(Home, '/')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(User, '/user')
