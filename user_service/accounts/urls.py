from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterView, UserDetailAPIView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:user_id>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]

