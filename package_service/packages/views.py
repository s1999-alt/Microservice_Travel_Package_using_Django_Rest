from rest_framework.views import APIView
from .models import Package
from .serializers import PackageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class PackageListCreateAPIView(APIView):
  def get(self, request):
    packages = Package.objects.all()
    serializer = PackageSerializer(packages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = PackageSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  
class PackageDetailsAPIView(APIView):
  def get(self, request, pk):
    package = get_object_or_404(Package, pk=pk)
    serializer = PackageSerializer(package)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    package = get_object_or_404(Package, pk=pk)
    serializer = PackageSerializer(package, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    return Response({"message": "Package deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

