from django.shortcuts import render
from state.models import State

# Create your views here.
def chart_view(request):
    states = State.objects.all()
    context = {
        "states": states,
    }
    return render(request, 'chart/chart.html', context)