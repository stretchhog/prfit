import wtforms
from flask import make_response, render_template
from flask_wtf import Form

from flask_restful import Resource
from google.appengine.ext.ndb import Key

from auth import auth
from control.base import base_auth_response
from main import app, api
from model import BaseCategory, BaseActivity


class TrackActivityForm(Form):
	category_key = wtforms.HiddenField(validators=[wtforms.validators.required()], widget=wtforms.widgets.HiddenInput())
	activity_key = wtforms.HiddenField(validators=[wtforms.validators.required()], widget=wtforms.widgets.HiddenInput())
	activity_name = wtforms.StringField('Activity', validators=[wtforms.validators.required()])

	tracked = wtforms.BooleanField('Tracked')


class TrackActivitiesForm(Form):
	track_activities = wtforms.FieldList(wtforms.FormField(TrackActivityForm))

	def __init__(self, activities, *args, **kwargs):
		super(TrackActivitiesForm, self).__init__(*args, **kwargs)
		for a in activities:
			self.track_activities.append_entry(data={
				'category_key': a.category_key.urlsafe(),
				'activity_key': a.key.urlsafe(),
				'activity_name': a.name,
				'tracked': a.tracked
			})


class TrackActivity(Resource):
	@auth.login_required
	def get(self, category_key):
		user_key = auth.current_user_key()
		data, _ = BaseActivity.get_dbs(user_key=user_key, category_key=Key(urlsafe=category_key))
		form = TrackActivitiesForm(data)

		app.logger.info(form.track_activities)
		return base_auth_response('track/track_activity.html', form=form, category_key=category_key, title='Track activities')

	def post(self):
		pass


class ChooseCategory(Resource):
	@auth.login_required
	def get(self):
		cats, _ = BaseCategory.get_dbs()
		return base_auth_response("track/track_category.html", categories=cats)


api.add_resource(TrackActivity, '/track_activity/<string:category_key>')
api.add_resource(ChooseCategory, '/choose_category')
