from django import forms
from . models import Movie_details

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie_details
        fields=['movie_name','movie_desc','movie_year','movie_image']
