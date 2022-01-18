from django.shortcuts import render

def load_csv(request):
    return render(request, "load_csv.html")