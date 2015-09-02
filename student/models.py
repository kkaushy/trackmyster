from django.db import models
from mongoengine import *
from django_mongodb_engine.contrib import MongoDBManager
from django.conf import settings


activity_db = settings.DATABASES.get('activity_db')
DB_NAME = activity_db.get('NAME')
connect(DB_NAME)


class Bus(models.Model):
	
	bus_no = models.CharField(max_length=20)
	device_id = models.CharField(max_length=50)	

	def __unicode__(self):
		return str(self.bus_no)

class Student(models.Model):

	tag_id = models.CharField(max_length=200, null=False)
	bus = models.ForeignKey(Bus)
	name = models.CharField(max_length=50)
	class_num = models.IntegerField(null=False)
	school = models.CharField(max_length=200)
	mobile_num = models.IntegerField(null=False)

	def __unicode__(self):
		return str(self.tag_id)

class Activity(DynamicDocument):
	
	tag_id = StringField()
	longitude = IntField(required=True)
	latitude = IntField(required=True)
	time = FloatField()
	boarding_type = IntField(required=True)
	object_type = BooleanField(default=False)

	def __str__(self):
		return str(self.tag_id)
