from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model


class BaseUser(model.Base):
	user_key = ndb.KeyProperty(kind=model.User, required=True)


class Category(BaseUser):
	name = ndb.StringProperty(required=True)


class Metric(BaseUser):
	name = ndb.StringProperty(required=True)


class BaseActivity(BaseUser, polymodel.PolyModel):
	category_key = ndb.KeyProperty(kind=Category, required=True)
	metric_key = ndb.KeyProperty(kind=Metric, required=True)

	name = ndb.StringProperty()
	description = ndb.StringProperty()


class CrossFit(BaseActivity):
	rxd = ndb.BooleanProperty()


class Record(BaseUser):
	activity = ndb.KeyProperty(kind=BaseActivity, required=True)
	category = ndb.KeyProperty(kind=Category, required=True)

	value = ndb.StringProperty(required=True)
	date = ndb.DateProperty()
	notes = ndb.StringProperty()
