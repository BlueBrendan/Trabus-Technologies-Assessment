from django.shortcuts import render
import csv
import os
import datetime
from django.conf import settings
from state.models import State, Statistic
import pandas as pd

def load_csv(request):
    states = set()
    # Read data from GitHub csv file and store in dataframe
    data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    # Take last 60 rows and store as a list
    data = data.values.tolist()
    # Data ingestor loops through every line in the CSV; this takes a very long time to complete
    for index, row in enumerate(data):
        # Check if state exists in database
        if index < 60:                
            try:
                state = State.objects.get(title=row[1].title())
                print(f"{state} exists")
            except State.DoesNotExist:
                State.objects.create(title=state.title())
            states.add(row[1])
        state = State.objects.get(title=row[1].title())
        # Check if statistic for date and state combination exists in database
        date = datetime.datetime(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:10]))
        try:                    
            stat = Statistic.objects.get(date=date, state=state)
            print(f"{stat} exists")
        except Statistic.DoesNotExist:
            Statistic.objects.create(date=date, state=state, cases=row[3], deaths=row[4]) 
    return render(request, "load_csv.html")