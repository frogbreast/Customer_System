from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

# サイト全体をログイン必須にする
class AuthMiddleware(MiddlewareMixin): 
    def process_response(self, request, response):
        if not request.user.is_authenticated and request.path != '/login/':
            return HttpResponseRedirect('/login/')
        return response
    