from datetime import datetime

from flask import make_response, render_template

from flask_restful import Resource
from main import api


def get_workout_categories():
	return ['Crossfit', 'Running', 'Weight Lifting']


data = [
	{
		"name": "Murph",
		"metric": "Time",
		"value": "49:20",
		'date': datetime.today().isoformat(),
		"rxd": True
	},
	{
		"name": "DT",
		"metric": "AMRAP",
		"value": "17",
		'date': datetime.today().isoformat(),
		"rxd": False
	}
]


class DefaultResponse(Resource):
	def get_response(self, template, **kwargs):
		return make_response(render_template(template, menu=get_workout_categories(), **kwargs))


class Home(DefaultResponse):
	def get(self):
		return self.get_response('home.html')


class Dashboard(DefaultResponse):
	def get(self):
		return self.get_response('dashboard.html', name="Crossfit", data=data)


class User(Resource):
	@staticmethod
	def get():
		return make_response(render_template('user.html'))


api.add_resource(Home, '/')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(User, '/user')
