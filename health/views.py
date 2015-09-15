from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.core.cache import cache
from django.db import connection

import string
import random


class HealthView(View):

    def get(self, request, *args, **kwargs):

        return HttpResponse(status=200)


class CacheHealthView(View):

    def get(self, request, *args, **kwargs):

        # Create a random cache key to avoid collision
        cache_key = ''.join(random.choice(string.ascii_letters) for _ in range(100))

        # Set the key in the cache and see if we can pull it out.
        cache.set(cache_key, 'works', 20)

        # If so, return 200
        if cache.get(cache_key) == 'works':
            return HttpResponse(status=200)

        # If not, return 404
        return HttpResponseNotFound()


class DBHealthView(View):

    def get(self, request, *args, **kwargs):

        with connection.cursor() as c:

            if connection.vendor == 'postgresql':
                from psycopg2 import OperationalError
                try:
                    c.execute('SELECT id FROM auth_user LIMIT 1')
                    result = c.fetchone()
                except OperationalError:
                    return HttpResponseServerError()
            else:
                c.execute('SELECT id FROM auth_user LIMIT 1')
                result = c.fetchone()

            return HttpResponse(result, status=200)
