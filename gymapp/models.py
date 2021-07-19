from django.db import models

# Create your models here.
class webusers(models.Model):
	username = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.username