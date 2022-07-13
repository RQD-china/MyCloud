from django.utils.deprecation import MiddlewareMixin
import json

class Decode(MiddlewareMixin):
    #请求中间件
    def process_request(self, request):
        if request.method == 'POST':
            request.data = json.loads(request.body)

    def process_response(self, request, response):
        print('响应')
        return response