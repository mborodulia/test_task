from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)


# app_name will help us do a reverse look-up latter.
urlpatterns = [path("", include(router.urls))]
