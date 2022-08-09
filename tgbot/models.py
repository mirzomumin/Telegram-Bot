from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=128, null=True, blank=True)
	image = models.URLField(null=True, blank=True)
	text = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title