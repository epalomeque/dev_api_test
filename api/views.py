from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from customer_order.views import get_result as customer_get_result
from api.serializers import CustomerSerializer


# Create your views here.
# @csrf_exempt
class CustomerView(APIView):
    """
    View to return Customer Order Data
    """
    def get(self, request, format=None, *args, **kwargs):
        res = customer_get_result()
        print('res ->', res)
        # serialized = CustomerSerializer(data=res, many=True)
        return Response(res)
        # return Response(serialized.data)


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
