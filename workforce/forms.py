from django import forms
from workforce.models import Clown

class PageForm(forms.ModelForm):

    model = Clown
    class Meta:
        model = Clown
        fields = '__all__'