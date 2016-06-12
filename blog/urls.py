from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^index2/$', 'blog.views.index2'),
    url(r'^1/$', 'blog.views.post_detail'),
    url(r'^api/v1/', include('blog.api.v1')),
]
