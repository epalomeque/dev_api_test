from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from customer_order.views import get_result as customer_get_result
from detect_change.views import get_result as change_get_result
from seasons.views import get_result as seasons_get_result


# Create your views here.
class CustomerView(APIView):
    """
    View to return Customer Order Data
    """
    def get(self, request, format=None, *args, **kwargs):
        res = customer_get_result()
        return Response(res)


class ChangesView(APIView):
    """
    View to return Changes Weather Data
    """
    def get(self, request, format=None, *args, **kwargs):
        res = change_get_result()
        return Response(res)


class SeasonsView(APIView):
    """
    View to return Seasons Data
    """
    def get(self, request, format=None, *args, **kwargs):
        res = seasons_get_result()
        return Response(res)
