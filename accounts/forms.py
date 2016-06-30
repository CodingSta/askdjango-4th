from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.EmailField(label='Email')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='Quiz', help_text='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer and answer != 6:
            raise forms.ValidationError('땡~!!!')
        return answer

