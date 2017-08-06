from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='topic')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural ='Topics'


class Post(models.Model):
	topic = models.ForeignKey(Topic)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title