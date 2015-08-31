from django.db import models


class Student(models.Model):

	tag_id = models.CharField(max_length=200, null=False)
	bus_no = models.CharField(max_length=200)
	name = models.CharField(max_length=50)
	class_num = models.IntegerField(null=False)
	school = models.CharField(max_length=200)	
	mobile_num = models.IntegerField(null=False)	

	def __unicode__(self):
		return str(self.tag_id)

class Travel(models.Model):
	
	student = models.ForeignKey(Student)
	category = models.CharField(max_length=5)
	time = models.IntegerField()

	def __unicode__(self):
		return str(self.student)