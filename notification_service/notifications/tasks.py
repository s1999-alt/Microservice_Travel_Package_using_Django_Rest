from celery import shared_task
import time


@shared_task
def send_booking_confirmation(email, package_name, booking_id):
    # Simulate sending email
    print("="*40)
    print("Sending Booking Confirmation")
    print(f"To: {email}")
    print(f"Package: {package_name}")
    print(f"Booking ID: {booking_id}")
    print("="*40)

    # Imagine actual email logic here
    time.sleep(2)

    return "Notification Sent"