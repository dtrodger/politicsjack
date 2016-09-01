from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse

from datetime import datetime


class Notification(models.Model):
	slug = models.SlugField(blank=True)
	image = models.ImageField(null = True, blank=True)
	title = models.CharField(max_length = 255, blank=True)
	description = models.CharField(max_length = 255, blank=True)
	expiration_date = models.DateTimeField(blank=True)
	created = models.DateTimeField(editable=False, blank=True)
	modified = models.DateTimeField(blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = datetime.now()
		self.modified = datetime.now()
		return super(Notification, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.title

@receiver(pre_save, sender=Notification)
def create_cause_slug(sender, instance, **kwargs):
	new_slug = slugify(instance.title)
	if len(Notification.objects.filter(slug=new_slug)) > 0:
		new_slug = new_slug+str(instance.id)
	instance.slug = new_slug