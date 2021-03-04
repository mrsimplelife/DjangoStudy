

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Profile


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?')

    def clean_answer(self):
        data = self.cleaned_data.get('answer')
        if data != 6:
            raise forms.ValidationError('wrong!!!!!')
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']
