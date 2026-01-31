from notification import EmailNotification, SMSNotification, PushNotification

def main():
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    if notification_type == "email":
        EmailNotification().send("Hello! This is a example.")
    elif notification_type == "sms":
        SMSNotification().send("Hello! This is a example.")
    elif notification_type == "push":
        return PushNotification().send("Hello! This is a example.")
    else:
        raise ValueError("Invalid notification type")


if __name__ == "__main__":
    main()
