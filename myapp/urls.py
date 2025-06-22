from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # This registers the 'books' endpoint

urlpatterns = [
    path('api/', include(router.urls)),  # This makes sure the router URLs are included under 'api/'
]
