from google.appengine.ext import db


class User(db.Model):
	name = db.StringProperty()


class BaseModel(db.Model):
	created = db.DateTimeProperty(auto_now_add=True)
	user = db.ReferenceProperty(User)


class Category(BaseModel):
	name = db.StringProperty()


class Record(BaseModel):
	name = db.StringProperty()
	value = db.StringProperty()
	date = db.DateTimeProperty()

	category = db.ReferenceProperty(Category)
	metric = db.ReferenceProperty(Metric)
	unit = db.ReferenceProperty(Unit)


class Metric(BaseModel):
	name = db.StringProperty()
	value = db.StringProperty()


class Unit(BaseModel):
	name = db.StringProperty()
	metric = db.ReferenceProperty(Metric, collection_name='units')
