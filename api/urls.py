from django.urls import include, path
from rest_framework import routers
from api.views import CustomerView, ListUsers

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('v1/users', ListUsers.as_view(), name='user_view'),
    path('v1/customers', CustomerView.as_view(), name='customer_view'),
    # path('v1/changes', ),
    # path('v1/seasons', seasons_view.as_view()),
]

