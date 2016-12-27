import json
import django.http

class JSONMiddleware(object):
    def process_request(self, request):
        if request.method != "POST":
            return None

        if 'application/json' not in request.META.get('CONTENT_TYPE', ''):
            return None

        body = request.body
        if not body:
            return None

        body = body.decode('utf8')

        json_data = json.loads(body)
        data = django.http.QueryDict('', mutable=True)
        data.update(json_data)
        if request.POST:
            data.update(request.POST)

        request.POST = data.copy()
