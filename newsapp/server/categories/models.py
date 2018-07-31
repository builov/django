from django.db import models

class Category(models.Model):

	name = models.CharField(max_length=255, unique=True)
	
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
	
		return self.name
