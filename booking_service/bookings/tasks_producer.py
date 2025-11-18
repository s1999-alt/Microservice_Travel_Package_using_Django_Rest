from celery import Celery

app = Celery("producer", broker="redis://redis:6379/0")

def send_booking_notification(email, package_name, booking_id):
    app.send_task(
        "notifications.tasks.send_booking_confirmation",
        args=[email, package_name, booking_id]
    )