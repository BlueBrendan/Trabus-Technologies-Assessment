import pandas as pd
import datetime
from state.models import State, Statistic

def daily_stat_update():
    today = datetime.date.today()
    today = today.strftime("%Y-%m-%d")
    print(today)
    # Read data from GitHub csv file and store in dataframe
    data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    # Take last 60 rows and store as a list
    data = data.values[-60:].tolist()
    remove = []
    for row in data:
        if str(row[0]) != today:
            remove.append(row)
    # Remove all rows from data that are not from today
    data = [row for row in data if row not in remove]
    print(data)
    # # Create statistic object for each row in data (data from today)
    # for row in data:
    #     date = datetime.datetime(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:10]))
    #     state = State.objects.get(state=row[1].title())
    #     try:
    #         stat = Statistic.objects.get(date=date, state=state)
    #     except Statistic.DoesNotExist:
    #         Statistic.objects.create(date=date, state=state, cases=row[3], deaths=row[4])
