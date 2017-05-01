from django import forms
from django.core import validators


class SuggestionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
    attrs={'type': 'text',
           'placeholder': ('Full Name')}))
    email = forms.EmailField(widget=forms.TextInput(
    attrs={'type': 'email',
           'placeholder': ('you@domain.com')}))
    #  verify_email = forms.EmailField(label="Please verify your email address")
    your_message = forms.CharField(widget=forms.TextInput(
    attrs={'type': 'text',
           'placeholder': ('Subject (optional but helpful)')}))
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                label="Leave empty",
                                validators=[validators.MaxLengthValidator(0)]
                                )

    # def clean(self):
    #    cleaned_data = super().clean()
    #    email = cleaned_data.get('email')
    #    verify = cleaned_data.get('verify_email')

    #    if email != verify:
    #        raise forms.ValidationError(
    #        "You need to enter the same email in both fields")
