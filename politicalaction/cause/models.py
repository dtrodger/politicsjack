from __future__ import unicode_literals

from django_resized import ResizedImageField
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User

from datetime import datetime

FREQUNCY_CHOICES = (
	("Daily","Daily"),
	("Weekly","Weekly"),
	("Monthly", "Monthly"),
	)

class Cause(models.Model):
	slug = models.SlugField()
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	created = models.DateTimeField(editable=False)
	modified = models.DateTimeField()
	verified = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('cause_detail', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = datetime.now()
		self.modified = datetime.now()
		return super(Cause, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.title

@receiver(pre_save, sender=Cause)
def create_cause_slug(sender, instance, **kwargs):
	new_slug = slugify(instance.title)
	if len(Cause.objects.filter(slug=new_slug)) > 0:
		new_slug = new_slug+str(instance.id)
	instance.slug = new_slug
