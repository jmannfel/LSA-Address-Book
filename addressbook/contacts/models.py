from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=16)
	email = models.EmailField(max_length=30)
	address = models.CharField(max_length=30)

	def get_full_name(self):         
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('contacts-view', kwargs={'pk': self.id})