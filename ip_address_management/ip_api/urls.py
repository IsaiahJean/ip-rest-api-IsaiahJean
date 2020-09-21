from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ipList', viewset=views.IpList)

urlpatterns = [
    path('', include(router.urls)),
    path(r'acquire/<int:pk>',views.IpAcquire.as_view(), name="ip_acquire"),
    path(r'available/<int:pk>',views.IpAvailable.as_view(), name="ip_available"),
]