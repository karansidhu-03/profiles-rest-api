from django.urls import path, include
from profiles_api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.ProfileViewSet)
router.register("feed", views.UserProfileFeedItemViewSet)


urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path("login/", views.UserLoginAPIView.as_view()),
    path("", include(router.urls)),
]
