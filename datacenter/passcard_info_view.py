from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    visits_by_this_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = list()
    for visit in visits_by_this_passcard:
        duration = visit.get_duration()
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": visit.format_duration(duration),
                "is_strange": visit.is_long()
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
