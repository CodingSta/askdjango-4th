from django.conf.urls import url
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from blog.models import Post


def post_list(request):
    return {'post_list': Post.objects.all(), }


def post_detail(request, pk):
    return get_object_or_404(Post, pk=pk)


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
