'''
This module will define the commonly used mixins for scroller app.
'''
import json

from django.http import HttpResponse


class JSONResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        ser_data = self.get_serialized_data(context)
        return HttpResponse(ser_data, content_type='application/json')

    def get_serialized_data(self, data):
        return json.dumps(data)
