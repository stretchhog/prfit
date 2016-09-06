from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model


class MetricType(model.Base):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	name = ndb.StringProperty(required=True)
	type = ndb.StringProperty(required=True)


class BaseMetric(model.Base, polymodel.PolyModel):
	user_key = ndb.KeyProperty(kind=model.User, required=True)


class DurationMetric(BaseMetric):
	value = ndb.IntegerProperty(required=True)


class DecimalMetric(BaseMetric):
	value = ndb.FloatProperty(required=True)


class CountMetric(BaseMetric):
	value = ndb.IntegerProperty(required=True)
