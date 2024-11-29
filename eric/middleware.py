# middleware.py
from django.http import HttpResponsePermanentRedirect
from django.conf import settings

class RedirectNonWWWToWWW:
    """
    Middleware to redirect non-www URLs to www URLs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        # Check if the domain is without 'www.'
        if not host.startswith('www.') and host != settings.SITE_DOMAIN:
            # Redirect to the www version
            return HttpResponsePermanentRedirect(f'https://www.{host}{request.get_full_path()}')

        response = self.get_response(request)
        return response
