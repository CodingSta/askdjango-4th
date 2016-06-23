from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^index2/$', 'blog.views.index2'),
    url(r'^(?P<category_pk>\d+)/(?P<pk>\d+)/$', 'blog.views.post_detail'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'),
    url(r'^(?P<pk>\w+)/$', 'blog.views.post_detail'),
    url(r'^api/v1/', include('blog.api.v1')),
]
