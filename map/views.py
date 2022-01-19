from django.shortcuts import render
from state.models import State, Statistic

# Create your views here.
def map_view(request):
    states = State.objects.all()
    data = {}
    for state in states:
        data[state.title] = state.death_rate
    print(data)
    context = {
        'data': data,
    }
    return render(request, 'map/map.html', context)