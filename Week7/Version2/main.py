from notification import EmailNotification, SMSNotification, PushNotification

def main():
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    notification = get_notification_type(notification_type)
    notification.send("Hello! This is a Factory Pattern example.")

def get_notification_type(notification_type: str):
    if notification_type == "email":
        return EmailNotification()
    elif notification_type == "sms":
        return SMSNotification()
    elif notification_type == "push":
        return PushNotification()
    else:
        raise ValueError("Invalid notification type")

if __name__ == "__main__":
    main()
