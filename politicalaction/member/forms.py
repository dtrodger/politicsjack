from django import forms

from .models import Member

class ProductModelForm(forms.ModelForm):
	publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)
	# description = forms.CharField(widget=forms.Textarea(
	# 		attrs={
	# 			"class": "my-custom-class",
	# 			"placeholder": "Description",
	# 			"some-attr": "this",
	# 		}
	# ))
	class Meta:
		model = Product
		fields = [
			"title",
			"description",
			"price",
		]
		widgets = {
			"description": forms.Textarea(
					attrs={
						"placeholder": "New Description"
					}
				),
			"title": forms.TextInput(
				attrs= {
					"placeholder": "Title"
				}
			)
		}


	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price <= 1.00:
			raise forms.ValidationError("Price must be greater than $1.00")
		elif price >= 100.00:
			raise forms.ValidationError("Price must be less than $100.00")
		else:
			return price

	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 3:
			return title
		else:
			raise forms.ValidationError("Title must be greater than 3 characters long.")















