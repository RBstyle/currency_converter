from rest_framework import routers
from django.urls import include, path

from converter import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("rates/", views.rates),
]
