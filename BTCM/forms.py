from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalogue.models import Catalogue, Collection


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
        fields = ['baseid', 'name', 'notes', 'image']

        help_texts = {
            'baseid': "This can be found on the base of the model, "
            "and is of the form '123', '12-34', 'a1', or '1A-23'."
        }


class AddCollectionForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Collection

        # specify fields to be used
        fields = ['mini']


class UpdateCollectionForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Collection

        # specify fields to be used
        fields = ['notes']
