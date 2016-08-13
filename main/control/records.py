import wtforms
import datetime
from flask import make_response, render_template, Response
from flask_wtf import Form

from flask_restful import Resource

from auth import auth
from main import api, app
from model import BaseCategory, BaseMetric, BaseActivity, BaseRecord


class RecordForm(Form):
	activity = wtforms.SelectField('Activity', [wtforms.validators.required()])
	category = wtforms.SelectField('Category', [wtforms.validators.required()])
	value = wtforms.StringField('Value', [wtforms.validators.required()])
	date = wtforms.DateField('Date', [wtforms.validators.optional()])
	notes = wtforms.TextAreaField('Notes', [wtforms.validators.optional()])

	def __init__(self, *args, **kwargs):
		super(RecordForm, self).__init__(*args, **kwargs)
		cats, _ = BaseCategory.get_dbs()
		print cats
		self.category.choices = [(cat.key.urlsafe(), cat.name) for cat in cats]


class Running(Resource):
	@auth.login_required
	def get(self):
		user_key = auth.current_user_key()
		cat = BaseCategory.get_by('name', 'Running')
		activities = BaseActivity.get_dbs(user_key=user_key, tracked=True, category_key=cat.key)[0]
		records = [BaseRecord.get_dbs(user_key=user_key, activity_key=a.key)[0] for a in activities]
		return make_response(render_template('records/running.html', activities=zip(activities, records)))


class InitActivities(Resource):
	@staticmethod
	def get():
		x, _ = BaseCategory.get_dbs()
		for y in x:
			y.key.delete()
		x, _ = BaseMetric.get_dbs()
		for y in x:
			y.key.delete()
		x, _ = BaseActivity.get_dbs()
		for y in x:
			y.key.delete()
		x, _ = BaseRecord.get_dbs()
		for y in x:
			y.key.delete()

		crossfit = BaseCategory(name="Crossfit").put()
		running = BaseCategory(name="Running").put()
		lifting = BaseCategory(name="Weight Lifting").put()

		dist = BaseMetric(name="Distance").put()
		time = BaseMetric(name="Time").put()
		amrap = BaseMetric(name="AMRAP").put()
		rep = BaseMetric(name="One-Rep Max").put()

		user = auth.current_user_key()
		fourm = BaseActivity(user_key=user, category_key=running, metric_key=time, name="400m", tracked=True).put()
		BaseActivity(user_key=user, category_key=running, metric_key=time, name="1k", tracked=True).put()
		BaseActivity(user_key=user, category_key=running, metric_key=time, name="1mi").put()
		fivek = BaseActivity(user_key=user, category_key=running, metric_key=time, name="5k", tracked=True).put()
		BaseActivity(user_key=user, category_key=running, metric_key=time, name="10k").put()
		BaseActivity(user_key=user, category_key=running, metric_key=time, name="Half Marathon").put()
		BaseActivity(user_key=user, category_key=running, metric_key=time, name="Marathon").put()
		BaseActivity(user_key=user, category_key=running, metric_key=dist, name="Longest Run").put()

		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Deadlift", tracked=True).put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Squat", tracked=True).put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Bench Press").put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Shoulder Press").put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Push Jerk", tracked=True).put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Power Clean").put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Squat Clean").put()
		BaseActivity(user_key=user, category_key=lifting, metric_key=rep, name="Power Snatch").put()

		BaseActivity(user_key=user, category_key=crossfit, metric_key=time, name="Grace", description=grace).put()
		BaseActivity(user_key=user, category_key=crossfit, metric_key=time, name="Fran", description=fran,
		             tracked=True).put()
		BaseActivity(user_key=user, category_key=crossfit, metric_key=time, name="Helen", description=helen).put()
		BaseActivity(user_key=user, category_key=crossfit, metric_key=time, name="Filthy 50", description=filthy).put()
		BaseActivity(user_key=user, category_key=crossfit, metric_key=amrap, name="Fight Gone Bad",
		             description=fgb).put()
		BaseActivity(user_key=user, category_key=crossfit, metric_key=time, name="DT", description=dt,
		             tracked=True).put()

		BaseRecord(user_key=user, category_key=running, activity_key=fourm, value="2:04",
		           date=datetime.date.today()).put()
		BaseRecord(user_key=user, category_key=running, activity_key=fivek, value="23:53",
		           date=datetime.date.today()).put()
		BaseRecord(user_key=user, category_key=running, activity_key=fivek, value="25:04",
		           date=datetime.date.today()).put()
		return Response(status=204)


api.add_resource(InitActivities, '/init')
api.add_resource(Running, '/record/running')

grace = """
30 power clean and push jerks
"""

fran = """
21-15-9 reps of:
95lbs/43kg Thrusters
Pull-ups
"""

dt = """
Five rounds of:
155lbs/70kg Deadlift, 12 reps
155lbs/70kg  Hang power clean, 9 reps
155lbs/70kg Push jerk, 6 reps
"""

helen = """
Three rounds of:
Run 400 meters
1.5pood/55lbs/25kg Kettlebell X 21 swings
12 Pull-ups
"""

filthy = """
50 Box jump, 24"/61cm box
50 Jumping pull-ups
50 Kettlebell swings, 1 pood/36lbs/16kg
Walking Lunges, 50 steps
50 Knees to elbows
50 Push press, 45lbs/21kg
50 Back extensions
50 Wall ball shots, 20lbs/9kg ball
50 Burpees
50 Double unders
"""

fgb = """
Three rounds of:
Wall-ball, 20lbs/9kg ball, 10ft/3m target (Reps)
Sumo deadlift high-pull, 75lbs/34kg (Reps)
Box Jump, 20"/51cm box (Reps)
Push-press, 75lbs/34kg (Reps)
Row (Calories)

In this workout you move from each of five stations after a minute.The clock does not reset or stop between exercises. This is a five-minute round from which a one-minute break is allowed before repeating. On call of "rotate", the athletes must move to next station immediately for best score. One point is given for each rep, except on the rower where each calorie is one point.
"""
