from django.conf.urls import include, url

# blog/api/v1.py
# blog/api/v2.py

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^1/$', 'blog.views.post_detail'),
    url(r'^api/v1/', include('blog.api.v1')),
]
