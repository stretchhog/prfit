from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model


class BaseUser(model.Base):
	user_key = ndb.KeyProperty(kind=model.User, required=True)


class BaseCategory(model.Base, polymodel.PolyModel):
	name = ndb.StringProperty(required=True)


class BaseMetric(model.Base, polymodel.PolyModel):
	name = ndb.StringProperty(required=True)


class BaseActivity(model.User, polymodel.PolyModel):
	category_key = ndb.KeyProperty(kind=BaseCategory, required=True)
	metric_key = ndb.KeyProperty(kind=BaseMetric, required=True)

	name = ndb.StringProperty()
	description = ndb.StringProperty()
	tracked = ndb.BooleanProperty(default=False)


class BaseRecord(BaseUser, polymodel.PolyModel):
	activity = ndb.KeyProperty(kind=BaseActivity, required=True)
	category = ndb.KeyProperty(kind=BaseCategory, required=True)

	value = ndb.StringProperty(required=True)
	date = ndb.DateProperty()
	notes = ndb.StringProperty()


class CrossfitRecord(BaseRecord):
	rxd = ndb.BooleanProperty()
