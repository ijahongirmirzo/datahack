from django.urls import include, path
from rest_framework import routers

from carprice.views import ProductRefreshApiView
from . import views

router = routers.DefaultRouter()
router.register(r'post_here', ProductRefreshApiView.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]