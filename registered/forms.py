from django import forms

from registered.models import Form
from registered.models import GENDER,CLASS,ITEMS


class RegistrationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER)
    school_grade = forms.ChoiceField(choices=CLASS)
    items = forms.ChoiceField(choices=ITEMS)
    class Meta:
        model = Form
        fields = "__all__" 
