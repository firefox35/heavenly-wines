from django import forms 
from djrichtextfield.widgets import RichTextWidget
from .models import Wine

class WineForm(forms.ModelForm):
    """ Form to create a wine """
    class Meta:
        model = Wine
        fields = ['title','year','type_of_wine', 'colour','country','description', 'image', 'image_alt',]

        widget = {
           'description': forms.Textarea(attrs={'rows': 5}), 
        }
        
        labels = {
            'title':'Wine Name',
            'year': 'Year of Wine',
            'type_of_wine': 'Type of Wine',
            'colour': 'Color of Wine',
            'country': 'Country of Orgin',
            'description': 'Description',
            'image': 'Wine Image',
            'image_alt': 'Describe Image',
        }
