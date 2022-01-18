from django.shortcuts import render
import csv
import os
import datetime
from django.conf import settings
from state.models import State, Statistic

def load_csv(request):
    states = set()
    with open(os.path.join(settings.BASE_DIR / 'templates', 'us-states.csv')) as fp:
        csv_file = csv.reader(fp, delimiter=",", quotechar='"')
        for index, row in enumerate(csv_file):
            if index > 0:
                # Check if statistic for date and state combination exists in database
                state = State.objects.get(title=row[1].title())
                date = datetime.datetime(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:10]))
                try:                    
                    stat = Statistic.objects.get(date=date, state=state)
                except Statistic.DoesNotExist:
                    Statistic.objects.create(date=date, state=state, cases=row[3], deaths=row[4])
                states.add(row[1])
    # Check if state exists in database
    for state in states:
        try:
            state = State.objects.get(title=state.title())
        except State.DoesNotExist:
            State.objects.create(title=state.title())
    return render(request, "load_csv.html")