from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import send_booking_confirmation


class TestNotification(APIView):
  def get(self, request):
      send_booking_confirmation.delay("test@example.com", "Bali Trip", 101)
      return Response({"message": "Notification triggered!"})
