from apps.mel.models.mel_item import MELItem
from apps.mel.models.mel_history import MELHistory


class MELService:

    @staticmethod
    def create_mel(data, user):
        mel = MELItem.objects.create(**data)

        MELHistory.objects.create(
            mel_item=mel,
            changed_by=user,
            old_status="NONE",
            new_status=mel.status,
            note="MEL created",
        )

        return mel

    @staticmethod
    def update_status(mel: MELItem, new_status: str, user):

        old_status = mel.status

        mel.status = new_status
        mel.save()

        MELHistory.objects.create(
            mel_item=mel,
            changed_by=user,
            old_status=old_status,
            new_status=new_status,
            note="Status updated",
        )

        return mel
