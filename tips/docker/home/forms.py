from django import forms
from .models import Image


# Define choices list
category_choices = [
    ('pool', 'pool'),
    ('ground', 'ground'),
    ]

city_choices = [
    ('paris', 'paris'),
    ('lille', 'lille'),
    ('lyon', 'lyon'),
    ('madrid', 'madrid'),
    ]


# Define the model forms
class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('title', 'category', 'city', 'selected_image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=category_choices, attrs={'class': 'form-control'}),
            'city': forms.Select(choices=city_choices, attrs={'class': 'form-control'}),
            }
