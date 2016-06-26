from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView
from blog.models import Post
from blog.forms import PostForm, PostModelForm


'''
def index(request):
    # messages.debug(request, 'hello messages framework.')
    # messages.error(request, 'error messages framework.')
    return render(request, 'blog/index.html')
'''

index = ListView.as_view(
    model=Post,
    queryset=Post.objects.all().order_by('-id'),
    template_name='blog/index.html')


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
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # ModelForm 에서만 지원되는 함수
            post.title = 'auto title'
            post.save()
            messages.success(request, '포스팅을 저장했습니다.')
            return redirect('blog:index')
    else:
        form = PostModelForm()

    return render(request, 'blog/post_form.html', {'legend': '새 포스팅 쓰기', 'form': form})
