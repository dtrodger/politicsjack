from django import forms

from .models import Notification

class NotificationCreationForm(forms.ModelForm):
	class Meta:
		model = Notification
		fields = [
			'cause',
			'title',
			'description',
			'location',
			'expiration_date',
		]