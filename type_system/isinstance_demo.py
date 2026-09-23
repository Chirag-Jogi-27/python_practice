class BaseNotification:
    pass


class EmailNotification(BaseNotification):
    def send_email(self):
        return "Email sent"


class SMSNotification(BaseNotification):
    def send_sms(self):
        return "SMS sent"


def dispatch(notification):
    if isinstance(notification, BaseNotification):
        print("Valid notification type received — processing...")

    if isinstance(notification, (EmailNotification, SMSNotification)):
        print("Supported channel — dispatching!")


dispatch(EmailNotification())
