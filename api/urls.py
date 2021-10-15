from django.urls import include, path
from rest_framework import routers
from api.views import CustomerView, ChangesView, SeasonsView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('v1/customers', CustomerView.as_view(), name='customer_view'),
    path('v1/changes', ChangesView.as_view(), name='changes_view'),
    path('v1/seasons', SeasonsView.as_view(), name='seasons_view'),
]

