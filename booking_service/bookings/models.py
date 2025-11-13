from django.db import models


class Booking(models.Model):
  user_id = models.IntegerField()
  package_id = models.IntegerField()
  booking_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, default='confirmed')
  total_price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"Booking #{self.id} - User {self.user_id} - Package {self.package_id}"
  
  
