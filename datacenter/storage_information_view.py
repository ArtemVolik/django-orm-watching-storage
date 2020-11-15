from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits = [
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": timezone.localtime(visit.entered_at),
                "duration": Visit.format_duration(visit.get_duration()),
            }
        ]
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
