from django.conf.urls import url, include
from rest_framework import routers
from simple import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
    url(r'^api/', include('simple.urls', namespace='api')),
    url(r'^index/',views.HomePageView.as_view(),name='index'),
   
   


]