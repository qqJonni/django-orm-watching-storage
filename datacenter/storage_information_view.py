from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits_serialized = list()

    for visit in non_closed_visits:
        duration = visit.get_duration()
        non_closed_visits_serialized.append({
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": visit.format_duration(duration),
            "is_strange": visit.is_long()
        })

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
