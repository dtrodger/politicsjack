from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import datetime

from legislative_body.models import LegislativeBody

class Politician(models.Model):
	name = models.CharField(max_length=255)
	ward = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	fax = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	website = models.CharField(max_length=255)
	office_address = models.CharField(max_length=255)
	office_city = models.CharField(max_length=255)
	office_state = models.CharField(max_length=255)
	office_zip = models.CharField(max_length=255)
	city_hall_phone = models.CharField(max_length=255)
	city_hall_address = models.CharField(max_length=255)
	legislative_body = models.ManyToManyField(LegislativeBody, blank=True)
	slug = models.SlugField()
	bio = models.CharField(max_length=255, blank=True)
	created = models.DateTimeField(editable=False)
	modified = models.DateTimeField()

	def get_absolute_url(self):
		return reverse('politician_detail', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = datetime.now()
		self.modified = datetime.now()
		return super(Politician, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.name

@receiver(pre_save, sender=Politician)
def create_cause_slug(sender, instance, **kwargs):
	new_slug = slugify(instance.name)
	if len(Politician.objects.filter(slug=new_slug)) > 0:
		new_slug = new_slug+str(instance.id)
	instance.slug = new_slug