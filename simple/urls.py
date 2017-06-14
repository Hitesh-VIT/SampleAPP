from django.conf.urls import url, include
from rest_framework import routers
from simple import views

router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)


urlpatterns = router.urls