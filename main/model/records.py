from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model


class BaseCategory(model.Base, polymodel.PolyModel):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	name = ndb.StringProperty(required=True)


class BaseMetric(model.Base, polymodel.PolyModel):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	name = ndb.StringProperty(required=True)


class BaseActivity(model.Base, polymodel.PolyModel):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	category_key = ndb.KeyProperty(kind=BaseCategory, required=True)
	metric_key = ndb.KeyProperty(kind=BaseMetric, required=True)

	name = ndb.StringProperty()
	description = ndb.StringProperty()
	tracked = ndb.BooleanProperty(default=False)


class BaseRecord(model.Base, polymodel.PolyModel):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	activity_key = ndb.KeyProperty(kind=BaseActivity, required=True)
	category_key = ndb.KeyProperty(kind=BaseCategory, required=True)

	value = ndb.StringProperty(required=True)
	date = ndb.DateProperty()
	notes = ndb.StringProperty()

	def is_valid_entry(self, form):
		return True


class CrossfitRecord(BaseRecord):
	rxd = ndb.BooleanProperty()
