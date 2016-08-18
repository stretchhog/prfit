# coding: utf-8

import flask
from control.base import base_auth_response
from flask import render_template, make_response
from datetime import datetime

from flask_restful import Resource

import config
from auth import auth
from main import app, api


###############################################################################
# Welcome
###############################################################################
class Welcome(Resource):
	def get(self):
		return base_auth_response('home.html')


###############################################################################
# Sitemap stuff
###############################################################################
@app.route('/sitemap.xml')
def sitemap():
	response = flask.make_response(flask.render_template(
			'sitemap.xml',
			lastmod=config.CURRENT_VERSION_DATE.strftime('%Y-%m-%d'),
	))
	response.headers['Content-Type'] = 'application/xml'
	return response


###############################################################################
# Warmup request
###############################################################################
@app.route('/_ah/warmup')
def warmup():
	# TODO: put your warmup code here
	return 'success'


class User(Resource):
	@staticmethod
	def get():
		return make_response(render_template('user.html', html_class="home"))


api.add_resource(Welcome, '/')
api.add_resource(User, '/user')
