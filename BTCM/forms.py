
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalogue.models import Catalogue

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# creating a form
class CatalogueForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Catalogue

        # specify fields to be used
        fields = ['baseid', 'name', 'notes']