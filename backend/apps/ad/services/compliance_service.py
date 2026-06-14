from datetime import date

from apps.ad.models.ad_compliance import ADCompliance
from apps.ad.models.airworthiness_directive import AirworthinessDirective


class ADComplianceService:

    @staticmethod
    def evaluate_compliance(ad_compliance: ADCompliance, aircraft):

        ad = ad_compliance.ad

        # ONE TIME AD
        if ad.compliance_type == "ONE_TIME":
            if ad_compliance.last_compliance_date:
                return ADCompliance.Status.COMPLIANT
            return ADCompliance.Status.DUE

        # RECURRING AD
        if ad.compliance_type == "RECURRING":

            if ad.interval_days and ad_compliance.last_compliance_date:
                days_passed = (date.today() - ad_compliance.last_compliance_date).days

                if days_passed > ad.interval_days:
                    return ADCompliance.Status.OVERDUE

                if days_passed > ad.interval_days * 0.8:
                    return ADCompliance.Status.DUE

        return ADCompliance.Status.COMPLIANT
