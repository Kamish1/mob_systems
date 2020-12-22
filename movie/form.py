from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class CollageForm(forms.ModelForm):
    class Meta:
        model = Collage
        fields = ['image']