from django import forms
from myuser.models import User_details

class SForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'
