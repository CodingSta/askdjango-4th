from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'blog/index.html')


index2 = TemplateView.as_view(template_name='blog/index.html')


def post_detail(request):
    pass
