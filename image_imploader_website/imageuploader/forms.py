from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {
            'image': ''
        }
# Compare this snippet from imageuploader/views.py:
# from django.shortcuts import render
