from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        #["name","age","image", "price"]
    #    '__all__'
