import wtforms
from flask import make_response, render_template
from flask_wtf import Form

from flask_restful import Resource
from google.appengine.ext.ndb import Key

from auth import auth
from main import app, api
from model import BaseCategory, BaseActivity


class TrackActivityForm(Form):
	category_name = wtforms.StringField('Category', validators=[wtforms.validators.required()])
	category_key = wtforms.StringField(validators=[wtforms.validators.required()], widget=wtforms.widgets.HiddenInput())
	activity_name = wtforms.StringField('Activity', validators=[wtforms.validators.required()])
	activity_key = wtforms.HiddenField(validators=[wtforms.validators.required()], widget=wtforms.widgets.HiddenInput())

	tracked = wtforms.BooleanField('Tracked')

	def __init__(self, activity, *args, **kwargs):
		super(TrackActivityForm, self).__init__(*args, **kwargs)
		self.category_name.data = activity.category_key.get().name
		self.category_key.data = activity.category_key.urlsafe()
		self.activity_name = activity.name
		self.activity_key = activity.key.urlsafe()
		self.tracked = activity.tracked


class TrackActivitiesForm(Form):
	track_activities = wtforms.FieldList(wtforms.FormField(TrackActivityForm))

	def __init__(self, activities, *args, **kwargs):
		super(TrackActivitiesForm, self).__init__(*args, **kwargs)
		for a in activities:
			form = TrackActivityForm(a)
			self.track_activities.append_entry(form)


class TrackActivity(Resource):
	@auth.login_required
	def get(self, key):
		user_key = auth.current_user_key()
		data, _ = BaseActivity.get_dbs(user_key=user_key, category_key=Key(urlsafe=key))
		form = TrackActivitiesForm(data)

		app.logger.info(form.track_activities)
		return make_response(render_template("track/track_activity.html", form=form))

	def post(self):
		pass


class ChooseCategory(Resource):
	@auth.login_required
	def get(self):
		cats, _ = BaseCategory.get_dbs()
		return make_response(render_template("track/track_category.html", categories=cats))


api.add_resource(TrackActivity, '/track_activity/<string:key>')
api.add_resource(ChooseCategory, '/choose_category')
