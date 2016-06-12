from django.conf.urls import url
from django.http import JsonResponse


def post_list(request):
    return JsonResponse({'name': 'chinseok'})


urlpatterns = [
    url(r'^posts/$', post_list),
]
