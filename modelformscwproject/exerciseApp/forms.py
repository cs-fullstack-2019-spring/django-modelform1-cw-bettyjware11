from django import forms
from .models import BlogPost

class NewUserForm(forms.ModelForm):
    # innerclass - class inside of class
    class Meta():
        # bind data to model
        model = BlogPost
        fields = ['title', 'text']
