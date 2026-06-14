from apps.ad.models.applicability_rule import ADApplicabilityRule


class ApplicabilityService:

    @staticmethod
    def is_applicable(ad, aircraft_type):

        rule = ADApplicabilityRule.objects.filter(
            ad=ad, aircraft_type=aircraft_type
        ).first()

        if not rule:
            return False

        return rule.is_applicable
