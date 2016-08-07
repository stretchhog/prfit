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
				"category": "Crossfit",
				"prs": [
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
					},
				]
			},
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
