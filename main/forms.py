from google.appengine.api import users

from models import Metric
from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired


class UnitForm(Form):
	unit = StringField('Unit', validators=[DataRequired()])
	metric = SelectField('Metric', validators=[DataRequired()], coerce=str)

	def __init__(self, **kwargs):
		super(UnitForm, self).__init__(**kwargs)
		user = users.get_current_user()
		self.metric.choices = Metric.get(user.user_id())

