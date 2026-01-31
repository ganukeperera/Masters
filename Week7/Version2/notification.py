
class EmailNotification():
    def send(self, message: str):
        print(f"📧 Email sent: {message}")

class SMSNotification():
    def send(self, message: str):
        print(f"📱 SMS sent: {message}")

class PushNotification():
    def send(self, message: str):
        print(f"🔔 Push notification sent: {message}")
