import wtforms
from control import Activities
from flask import make_response, render_template, flash, redirect
from flask_wtf import Form

from flask_restful import Resource
from google.appengine.ext.ndb import Key

from auth import auth
from control.base import base_auth_response
from main import app, api
from model import BaseCategory, BaseActivity


class TrackActivityForm(Form):
	category_key = wtforms.HiddenField(validators=[wtforms.validators.required()])
	activity_key = wtforms.HiddenField(validators=[wtforms.validators.required()])
	activity_name = wtforms.StringField('Activity')

	tracked = wtforms.BooleanField('Tracked')


class TrackActivitiesForm(Form):
	activities = wtforms.SelectMultipleField()

	def __init__(self, data, *args, **kwargs):
		super(TrackActivitiesForm, self).__init__(*args, **kwargs)
		self.activities.choices = [(d.key.urlsafe(), d.name) for d in data]
		self.activities.data = [d.key.urlsafe() for d in data if d.tracked]


class TrackActivity(Resource):
	def response(self, template, form, category_key):
		return base_auth_response('track/track_activity.html', form=form, category_key=category_key,
		                          title='Track activities')

	def get_form(self, category_key):
		user_key = auth.current_user_key()
		data, _ = BaseActivity.get_dbs(user_key=user_key, category_key=Key(urlsafe=category_key))
		form = TrackActivitiesForm(data)
		return form

	@auth.login_required
	def get(self, category_key):
		return self.response('track/track_activity.html', self.get_form(category_key), category_key)

	@auth.login_required
	def post(self, category_key):
		form = self.get_form(category_key)
		if form.validate_on_submit():
			for a in form.data['track_activities']:
				activity = Key(urlsafe=a['activity_key']).get()
				activity.tracked = a['tracked']
				activity.put()
			flash('Update successful', category='success')
			return redirect(api.url_for(Activities, category_key=category_key))
		flash('Update not successful', category='warning')
		return self.response('track/track_activity.html', form, category_key)


class ChooseCategory(Resource):
	@auth.login_required
	def get(self):
		cats, _ = BaseCategory.get_dbs()
		return base_auth_response("track/track_category.html", categories=cats)


api.add_resource(TrackActivity, '/track_activity/<string:category_key>')
api.add_resource(ChooseCategory, '/choose_category')
