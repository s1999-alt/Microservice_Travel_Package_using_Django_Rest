from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializers


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





