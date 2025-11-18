from django.urls import path
from .views import TestNotification

urlpatterns = [
    path("test/", TestNotification.as_view()),
]