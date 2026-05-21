from apps.users.models.user import User


def get_user_by_id(user_id: int):
    return User.objects.filter(id=user_id).first()


def get_all_engineers():
    return User.objects.filter(role="ENGINEER", is_active_engineer=True)
