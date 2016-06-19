from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import JsonResponse
from blog.encoder import JSONEncoder


class JsonMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, (dict, list, tuple, set, QuerySet, Model)):
            return JsonResponse(response, encoder=JSONEncoder, safe=False)
        return response
