from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from backend.api import views, serializers

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/usertasks', views.UserTaskViewSet)
urlpatterns = [
        path('', include(router.urls)),
        ]
