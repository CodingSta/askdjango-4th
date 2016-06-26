from django import forms
from django.core.validators import MinLengthValidator
from blog.models import Post


class PostForm(forms.Form):
    title = forms.CharField(validators=[MinLengthValidator(3)])
    content = forms.CharField(widget=forms.Textarea)

    # forms.Form 에는 없지만, ModelForm 과 유사한 인터페이스를 만들어주기 위해 구현
    def save(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        post = Post.objects.create(title=title, content=content)
        return post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
