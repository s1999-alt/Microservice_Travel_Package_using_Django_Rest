from django.urls import path
from .views import PackageListCreateAPIView, PackageDetailsAPIView

urlpatterns = [
  path('packages/', PackageListCreateAPIView.as_view(), name='package-list-create'),
  path('package/<int:pk>/', PackageDetailsAPIView.as_view(), name='package-detail'),
]
