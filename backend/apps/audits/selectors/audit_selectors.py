from apps.audits.models import AuditLog


def get_model_audits(model_name: str, object_id: str):

    return AuditLog.objects.filter(
        model_name=model_name,
        object_id=object_id,
    ).order_by("-timestamp")


def get_user_audits(user_id: int):

    return AuditLog.objects.filter(user_id=user_id).order_by("-timestamp")
