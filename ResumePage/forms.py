from django import forms

from ResumePage.models import Resume
import re


def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(pattern, email))


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'profile_summary', 'education', 'skills',
                  'work_experience', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def clean_full_name(self, *args, **kwargs):
        full_name = self.cleaned_data.get('full_name')
        for character in full_name:
            if not character.isalpha():
                raise forms.ValidationError("Please enter a valid full name")
        return full_name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not is_valid_email(email):
            raise forms.ValidationError("Please enter a valid email address")
        return email

    def clean_phone_number(self, *args, **kwargs):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) < 11 or not phone_number.isdigit():
            raise forms.ValidationError("Please enter a valid phone number")
        return phone_number
