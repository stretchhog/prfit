import wtforms
from flask_wtf import Form

from model import Category


class RecordForm(Form):
	activity = wtforms.SelectField('Activity', [wtforms.validators.required()])
	category = wtforms.SelectField('Category', [wtforms.validators.required()])
	value = wtforms.StringField('Value', [wtforms.validators.required()])
	date = wtforms.DateField('Date', [wtforms.validators.optional()])
	notes = wtforms.TextAreaField('Notes', [wtforms.validators.optional()])

	def __init__(self, *args, **kwargs):
		super(RecordForm, self).__init__(*args, **kwargs)
		cats, _, _ = Category.get_dbs()
		print(cats)
		self.category.choices = [(cat.key.urlsafe(), cat.name) for cat in cats]
