from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile


class SignupForm(UserCreationForm):
    username = forms.EmailField(label='Email')
    address = forms.CharField(required=False)
    phone = forms.CharField(required=False)

    def save(self):
        user = super(SignupForm, self).save(commit=False)
        user.email = user.username
        user.save()

        address = self.cleaned_data.get('address', '')
        phone = self.cleaned_data.get('phone', '')
        Profile.objects.create(user=user, address=address, phone=phone)

        return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='Quiz', help_text='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer and answer != 6:
            raise forms.ValidationError('땡~!!!')
        return answer

