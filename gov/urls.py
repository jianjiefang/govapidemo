from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from gov import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'gov', views.GovViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'group', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]

