from apps.notifications.models.notification import Notification


class NotificationService:

    @staticmethod
    def create_notification(title, message, type, aircraft=None, user=None, **kwargs):
        """Create a Notification and accept either model instances or ids for aircraft/user.

        Keeps a backward-compatible signature while allowing callers to pass
        `aircraft` and `user` as either objects or integer IDs.
        """

        data = {
            "title": title,
            "message": message,
            "type": type,
        }

        # Accept user as object or id
        if user is not None:
            if isinstance(user, int):
                data["user_id"] = user
            else:
                data["user"] = user

        # Accept aircraft as object or id
        if aircraft is not None:
            if isinstance(aircraft, int):
                data["aircraft_id"] = aircraft
            else:
                data["aircraft"] = aircraft

        # Merge any additional allowed kwargs (future-proof)
        allowed_extra = {k: v for k, v in kwargs.items() if k in [
            "status", "sent_at"]}
        data.update(allowed_extra)

        return Notification.objects.create(**data)
