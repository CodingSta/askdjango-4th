import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.query import QuerySet


class JSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if hasattr(o, 'as_dict'):
            return o.as_dict()
        elif hasattr(o, 'as_list'):
            return o.as_list()
        elif isinstance(o, Model):
            return {
                'id': o.id,
                'message': '{} is not JSON serializable'.format(o.__class__),
            }
        elif isinstance(o, QuerySet):
            return tuple(o)
        else:
            return super(MyJSONEncoder, self).default(o)
