from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
import requests
from django.shortcuts import get_object_or_404


USER_SERVICE_URL = "http://user_service:8000/api/users/"
PACKAGE_SERVICE_URL = "http://package_service:8000/api/packages/"


class BookingListCreateAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    """
    Create booking after verifying:
    1. User exists via User Service
    2. Package exists via Package Service
    """
    user_id = request.data.get('user_id')
    package_id = request.data.get('package_id')

    # Step 1: Verify User
    user_response =  requests.get(f"{USER_SERVICE_URL}{user_id}/")
    if user_response.status_code != 200:
      return Response({"error": "Invalid User"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Step 2: Verify Package
    package_response = requests.get(f"{PACKAGE_SERVICE_URL}{package_id}/")
    if package_response.status_code != 200:
      return Response({"error": "Inavalid Package"}, status=status.HTTP_400_BAD_REQUEST)
    
    package_data = package_response.json()
    total_price = package_data.get('price', 0.0)
  
    # Step 3: Create Booking
    booking = Booking.objects.create(
      user_id=user_id,
      package_id=package_id,
      total_price=total_price,
    )
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  
  def put(self, request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = request.data.get('status', booking.status)
    booking.save()
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_200_OK)


  def delete(self, request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return Response({"message": "Booking deleted"}, status=status.HTTP_204_NO_CONTENT)







