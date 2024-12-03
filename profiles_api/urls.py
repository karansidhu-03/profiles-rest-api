from django.urls import path, include
from profiles_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("viewset", views.HelloViewSet, basename="viewset")
router.register("profile", views.ProfileViewSet)

urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path("", include(router.urls)),
]
