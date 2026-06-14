from apps.aircraft.models.aircraft import Aircraft


def get_all_aircraft():
    return Aircraft.objects.select_related(
        "aircraft_type",
        "operator",
    )


def get_active_aircraft():
    return Aircraft.objects.filter(status="ACTIVE")


def get_aircraft_by_tail_number(tail_number: str):
    return (
        Aircraft.objects.filter(tail_number=tail_number)
        .select_related(
            "aircraft_type",
            "operator",
        )
        .first()
    )
