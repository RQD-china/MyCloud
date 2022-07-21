from django.utils.deprecation import MiddlewareMixin
import json

class Decode(MiddlewareMixin):
    # 请求中间件
    def process_request(self, request):
        if request.method == 'POST' and request.META.get('CONTENT_TYPE') == 'application/json':
            request.data = json.loads(request.body)

    # 响应中间件
    def process_response(self, request, response):
        return response