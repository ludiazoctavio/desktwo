from django.db import models


class Department(models.Model):

	name = models.CharField(max_length=200)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Company(models.Model):
	
	#client
	name = models.CharField(max_length=200)
	acronym = models.CharField(max_length=200)
	company = models.ManyToManyField(Department)
	#phone

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


#class Location(models.Model):