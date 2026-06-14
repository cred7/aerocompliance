from apps.aircraft.models.aircraft import Aircraft
from apps.audits.services.audit_service import AuditService
import logging

logging.basicConfig(level=logging.INFO)


class AircraftService:

    @staticmethod
    def create_aircraft(validated_data, user):

        if user is None:
            raise ValueError("User must be provided for audit logging.")
        aircraft = Aircraft.objects.create(**validated_data)
        logging.info(
            f"Aircraft created with ID: {aircraft.id} and Tail Number: {aircraft.tail_number} by User: {user.username}"
        )

        AuditService.log_create(
            user=user,
            instance=aircraft,
            after={
                "tail_number": aircraft.tail_number,
                "status": aircraft.status,
            },
        )

        return aircraft

    @staticmethod
    def update_aircraft(instance, validated_data, user):
        if user is None:
            raise ValueError("User must be provided for audit logging.")

        logging.info(
            f"Aircraft updated with ID: {instance.id} and Tail Number: {instance.tail_number} by User: {user.username}"
        )
        before = {
            "tail_number": instance.tail_number,
            "status": instance.status,
        }

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        after = {
            "tail_number": instance.tail_number,
            "status": instance.status,
        }

        AuditService.log_update(
            user=user,
            action="UPDATE",
            instance=instance,
            before=before,
            after=after,
        )

        return instance

    @staticmethod
    def delete_aircraft(instance, user):
        if user is None:
            raise ValueError("User must be provided for audit logging.")

        before = {
            "tail_number": instance.tail_number,
            "status": instance.status,
        }

        instance.delete()

        logging.info(
            f"Aircraft deleted with ID: {instance.id} and Tail Number: {instance.tail_number} by User: {user.username}"
        )

        AuditService.log_delete(
            user=user,
            action="DELETE",
            instance=instance,
            before=before,
        )
