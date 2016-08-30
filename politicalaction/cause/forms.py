from django import forms

from .models import Cause

class CauseCreationForm(forms.ModelForm):
	class Meta:
		model = Cause
		fields = [
			'title',
			'description',
		]