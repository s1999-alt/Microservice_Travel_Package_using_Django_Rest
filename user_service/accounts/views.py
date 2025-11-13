from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(
        {'message': "User registered successfully!", "data": serializer.data},
        status=status.HTTP_201_CREATED
      )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request, user_id):
    try:
      user = User.objects.get(id=user_id)
      serializer = UserSerializers(user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
      return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)






