from django.shortcuts import render
from django.http import JsonResponse
from .models import State, Statistic
from django.core import serializers

# Create your views here.
def load_state_data(request, state_name):
    print(state_name)
    state = State.objects.get(title=state_name.title())
    stats = Statistic.objects.filter(state=state)
    data = [[x.date, x.cases, x.deaths] for x in stats]
    return JsonResponse({
        "data": data,
    })