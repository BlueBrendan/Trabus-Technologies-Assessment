from django.shortcuts import render

# Create your views here.
def chart_view(request):
    return render(request, 'chart/chart.html')