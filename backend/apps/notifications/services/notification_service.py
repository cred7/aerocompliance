from apps.notifications.models.notification import Notification


class NotificationService:

    @staticmethod
    def create_notification(title, message, type):

        return Notification.objects.create(
            # user=user,
            title=title,
            message=message,
            type=type,
        )
