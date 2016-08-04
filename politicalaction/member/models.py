from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User

from datetime import datetime


PREFIX_CHOICES = (
		("Mr.","Mr."),
		("Mrs.","Mrs"),
		("Mr.","Mr."),
		)

class Member(models.Model):
	username = models.CharField(max_length=255)
	prefix = models.CharField(max_length=255, choices = PREFIX_CHOICES)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	slug = models.SlugField()
	bio = models.CharField(max_length=255)
	created = models.DateTimeField(editable=False)
	modified = models.DateTimeField()

	def get_absolute_url(self):
		return reverse('cause_detail', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = datetime.now()
		self.modified = datetime.now()
		return super(Member, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.username

@receiver(pre_save, sender=Member)
def create_cause_slug(sender, instance, **kwargs):
	new_slug = slugify(instance.username)
	if len(Member.objects.filter(slug=new_slug)) > 0:
		new_slug = new_slug+str(instance.id)
	instance.slug = new_slug