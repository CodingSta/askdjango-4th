from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^(?P<category_pk>\d+)/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/20/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\w+)/$', views.post_detail, name='post_detail'),
    url(r'^api/v1/', include('blog.api.v1', namespace='api_v1')),
]
