from django import forms
from django.core.validators import MinLengthValidator
from blog.models import Post


class PostForm(forms.Form):
    title = forms.CharField(validators=[MinLengthValidator(3)])
    content = forms.CharField(widget=forms.Textarea)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
