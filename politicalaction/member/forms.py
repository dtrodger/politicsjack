from django import forms

from .models import Member

class MemberModelForm(forms.ModelForm):
	# publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)
	# description = forms.CharField(widget=forms.Textarea(
	# 		attrs={
	# 			"class": "my-custom-class",
	# 			"placeholder": "Description",
	# 			"some-attr": "this",
	# 		}
	# ))
	class Meta:
		model = Member
		fields = [
			"prefix",
			"first_name",
			"last_name",
			"bio",
		]
		widgets = {
			"bio": forms.Textarea(
					attrs={
						"placeholder": "Tell Us About Yourself"
					}
				)
		}


	# def clean_price(self):
	# 	price = self.cleaned_data.get("price")
	# 	if price <= 1.00:
	# 		raise forms.ValidationError("Price must be greater than $1.00")
	# 	elif price >= 100.00:
	# 		raise forms.ValidationError("Price must be less than $100.00")
	# 	else:
	# 		return price

	# def clean_title(self):
	# 	title = self.cleaned_data.get("title")
	# 	if len(title) > 3:
	# 		return title
	# 	else:
	# 		raise forms.ValidationError("Title must be greater than 3 characters long.")















