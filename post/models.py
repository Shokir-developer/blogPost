from django.db import models
from django.contrib.auth.models import User

class Yangiliklar(models.Model):
	STATUS = (
		(0, 'Draft'),
		(1, 'Publish')
		)

	title = models.CharField(max_length=200, null=True)
	main_content = models.CharField(max_length=200, null=True)
	content = models.TextField(null=True)
	author = models.ForeignKey(User, on_delete = models.SET_NULL, blank=True, null=True)
	sana = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=100)
	status = models.IntegerField(default=0, choices = STATUS)
	image = models.ImageField(upload_to='images', null=True)


	def __str__(self):
		return self.title