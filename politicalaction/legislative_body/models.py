from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

from datetime import datetime

from event.models import Event

class LegislativeBody(models.Model):
	slug = models.SlugField()
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	events = models.ManyToManyField(Event, blank=True)
	created_on = models.DateTimeField(editable=False)
	modified_on = models.DateTimeField()
	verified_on = models.BooleanField(default=False)

	# def get_absolute_url(self):
	# 	return reverse('event_detail', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.id:
			self.created_on = datetime.now()
		self.modified_on = datetime.now()
		return super(LegislativeBody, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.name

@receiver(pre_save, sender=LegislativeBody)
def create_cause_slug(sender, instance, **kwargs):
	new_slug = slugify(instance.name)
	if len(LegislativeBody.objects.filter(slug=new_slug)) > 0:
		new_slug = new_slug+str(instance.id)
	instance.slug = new_slug