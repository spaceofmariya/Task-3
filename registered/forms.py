from django import forms
from registered.models import Form
from registered.models import GENDER,CLASS,ITEMS



class RegistrationForm(forms.ModelForm):
    gender = forms.RadioSelect(choices=GENDER)
    class_ = forms.ChoiceField(choices=CLASS)
    items = forms.ChoiceField(choices=ITEMS)
    class Meta:
        model = Form
        fields = '__all__' 
        # widgets = {
        #     "first_name": forms.TextInput(),
        #     "last_name": forms.TextInput(),
        #     "date_of_birth": forms.DateInput(),
        #     "gender": forms.RadioSelect(),
        #     "class_": forms.Select(),
        #     "email": forms.EmailInput(),
        #     "contact_number": forms.TextInput(),
        #     "item": forms.Select(),
        # }