'''
Created on Feb 25, 2012

@author: Joel Haasnoot
'''
from django.conf import settings
from django.utils import translation

class ForceLanguageMiddleware:

    def process_request(self, request):
        if request.session.get('django_language'):
            language = translation.get_language_from_request(request)
        elif request.COOKIES.get('django_language'):
            language = translation.get_language_from_request(request)
        else:
            language = 'nl'
        #language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
        