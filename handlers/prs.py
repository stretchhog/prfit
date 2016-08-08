import json

from datetime import datetime

from flask import make_response, render_template, Response

from flask_restful import Resource
from main import api


class CurrentPR(Resource):
	@staticmethod
	def get():
		data = {"prs": [
			{
				"category": "Running",
				"prs": [
					{
						"name": "1k",
						"metric": "Time",
						'date': datetime.today().isoformat(),
						"value": "4:12"
					},
					{
						"name": "Farthest run",
						"metric": "Distance",
						'date': datetime.today().isoformat(),
						"value": "11.2"
					},
				]
			},
			{
				"category": "Weight Lifting",
				"prs": [
					{
						"name": "Back Squat",
						"metric": "One Rep Max",
						'date': datetime.today().isoformat(),
						"value": "100"
					},
					{
						"name": "Front Squat",
						"metric": "One Rep Max",
						'date': datetime.today().isoformat(),
						"value": "55"
					},
				]
			},
		]}
		return Response(json.dumps(data), 200, mimetype="application/json")


api.add_resource(CurrentPR, '/api/current_prs')
