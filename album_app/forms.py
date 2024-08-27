from django import forms
from .models import Album

class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        
        widgets = {
            'release_date' : forms.DateInput(attrs= {'type' : 'date'})
        }