import json

import requests
from django.views.generic import TemplateView

from .mixins import JSONResponseMixin


class ImageView(JSONResponseMixin, TemplateView):
    template_name = 'scroll.html'
    # URL to collect image data.
    IMAGES_URI = 'http://192.254.141.167/~fstech/pic.php'

    def render_to_response(self, context, **response_kwargs):
        # Based on the content type, response will be generated.
        content_type = self.request.META['CONTENT_TYPE']
        if content_type == 'application/json':
            images_data = self.fetch_and_return_images()
            return self.render_to_json_response(images_data,
                                                **response_kwargs)
        else:
            return super(ImageView, self).render_to_response(context,
                                                             **response_kwargs)

    def fetch_and_return_images(self):
        """ This method is used to fetch the image info and return the json."""
        response = requests.get(self.IMAGES_URI)
        return json.loads(response.content)
