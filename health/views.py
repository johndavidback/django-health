from django.views.generic import View
from django.http import HttpResponse


class HealthView(View):

    def get(self, request, *args, **kwargs):

        return HttpResponse(status=200)
