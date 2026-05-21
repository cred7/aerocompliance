from apps.audits.models import AuditLog
import logging

logger = logging.getLogger(__name__)


class AuditService:

    @staticmethod
    def log_create(user, instance, after=None):
        AuditLog.objects.create(
            user=user if user and user.is_authenticated else None,
            action=AuditLog.Action.CREATE,
            model_name=instance.__class__.__name__,
            object_id=str(instance.pk),
            before=None,
            after=after,
        )

    @staticmethod
    def log_update(user, instance, before_data=None, after=None):
        AuditLog.objects.create(
            user=user if user and user.is_authenticated else None,
            action=AuditLog.Action.UPDATE,
            model_name=instance.__class__.__name__,
            object_id=str(instance.pk),
            before=before_data,
            after=after,
        )

    @staticmethod
    def log_delete(user, instance, before=None):
        AuditLog.objects.create(
            user=user if user and user.is_authenticated else None,
            action=AuditLog.Action.DELETE,
            model_name=instance.__class__.__name__,
            object_id=str(instance.pk),
            before=before or instance.__dict__,
            after=None,
        )
