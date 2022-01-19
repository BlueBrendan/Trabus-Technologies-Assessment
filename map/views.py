from django.shortcuts import render
from django.http import JsonResponse
from state.models import State, Statistic

# Create your views here.
def map_view(request):
    states = State.objects.all()
    data = {}
    for state in states:
        data[state.title.lower()] = state.death_rate
    print(data)
    context = {
        'state_data': data,
    }
    return render(request, 'map/map.html', context)