from django.shortcuts import render
from django.http import JsonResponse
from state.models import State, Statistic
import numpy as np

# Create your views here.
def map_view(request):
    states = State.objects.all()
    data = {}
    death_rates = []
    for state in states:
        data[state.title.lower()] = state.death_rate
        death_rates.append(state.death_rate)
    # Calculate percentiles
    death_rates = np.array(death_rates)
    low = np.percentile(death_rates, 20)
    medium = np.percentile(death_rates, 40)
    high = np.percentile(death_rates, 60)
    veryHigh = np.percentile(death_rates, 80)
    context = {
        'state_data': data,
        'percentiles': [low, medium, high, veryHigh],
    }
    return render(request, 'map/map.html', context)