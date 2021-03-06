from django import forms
from django.core import validators

def check_name(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with z')

class FormName(forms.Form):
    name = forms.CharField(validators = [check_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Emails must be the same")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Caught Bot!!')
    #     else:
    #         return botcatcher
