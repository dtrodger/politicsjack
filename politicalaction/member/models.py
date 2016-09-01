from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import datetime
from cause.models import Cause


PREFIX_CHOICES = (
		("Mr.","Mr."),
		("Mrs.","Mrs"),
		("Mr.","Mr."),
		)

class Member(models.Model):
	slug = models.SlugField()
	user = models.OneToOneField(User)
	prefix = models.CharField(max_length=255, choices = PREFIX_CHOICES)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	bio = models.CharField(max_length=255, blank=True)
	causes = models.ManyToManyField(Cause, related_name="cause_member", blank = True)
	key_cause_member = models.ManyToManyField(Cause, related_name="cause_key_member", blank = True)
	moderator = models.ManyToManyField(Cause, related_name="cause_moderator", blank = True)
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