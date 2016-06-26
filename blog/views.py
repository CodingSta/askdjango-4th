from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from blog.models import Post
from blog.forms import PostForm, PostModelForm


def index(request):
    return render(request, 'blog/index.jinja2')


index2 = TemplateView.as_view(template_name='blog/index.html')


def post_detail(request, pk, category_pk=None):
    return HttpResponse('''pk = {}, category_pk = {}

<p>request.GET = {}</p>
<p>request.POST = {}</p>
<p>request.FILES = {}</p>
'''.format(pk, category_pk,
        repr(request.GET.getlist('a')),
        repr(request.POST),
        repr(request.FILES)))


def post_new(request):
    errors = []
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()  # ModelForm 에서만 지원되는 함수
            return redirect('blog:index')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})
