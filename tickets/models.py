from django.db import models
from ckeditor.fields import RichTextField
from companies.models import Company, Department


STATUS_CHOICES = (
	(1, 'Open'),
	(2, 'Assigned'),
	(3, 'Pending'),
	(4, 'Closed'),
)

class Area(models.Model):
	
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Item(models.Model):
	
	name = models.CharField(max_length=200)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Ticket(models.Model):


	#requesttype
	subject = models.CharField(max_length=200)
	requestdetail = RichTextField()
	#client
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	#location
	departament = models.ForeignKey(Department, on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	#priority
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
	#createdby
	#tech
	#assettype
	opendate = models.DateTimeField('date published')
	#firstresponsedate
	#lastupdate
	#closedate
	#scheduleddatefrom
	#scheduleddateto
	#duedate

	class Meta:
		ordering = ['opendate']

	def __unicode__(self):
		return self.subject

	def __str__(self):
		return self.subject


#class Notes(models.Model):