from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from blog.models import Post


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
        title = request.POST['title']
        content = request.POST['content']
        if not title:
            errors.append('제목을 넣어주세요.')
        if len(title) < 5:
            errors.append('제목을 5자 이상 입력해주세요.')
        if not content:
            errors.append('내용을 넣어주세요.')

        if not errors:
            Post.objects.create(title=title, content=content)
            return redirect('blog:index')

    return render(request, 'blog/post_form.html', {'errors': errors})
