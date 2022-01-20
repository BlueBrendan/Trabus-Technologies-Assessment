# Trabus-Technologies-Assessment

# Data Ingestor
The data ingestor code is written in the function "load_csv" in TrabusAssessment/views.py. The code uses Pandas to read the NY CSV. For each line in the CSV, the code will check the state, date, number of cases, and number of deaths. If the state does not exist in the database, it will create the state object with the title. If the statistic object does not exist (date, state, cases, deaths), it will create it. This continues until the end of the CSV is reached

The view can be run by navigating to the URL /load_csv

# Database
The database stores records of two models called State and Statistic. State is used to represent each state and has a title field corresponding to the state name (ex. California) as well as a float field for the total death rate (total cases/total deaths). Statistic is used to represent each state's total case and death count for a specfiic day. It has a date field, two integer fields for cases and deaths, and a foreign key pointing to a State. The cron job is setup so that every day at 11:00PM, the code will collect the day's records from the CSV for all states and save them to the database if they do not exist already. It will then recalculate the death rate for each state using the latest record.   

The postgres database is stored on the cloud through elephantsql, so running the data ingestor code to store the records into the database should not be necessary

# Interactive Plot
The interactive plot uses a dropdown list of states to display new cases. When a state is selected, all database records for that state (containing date and total cases) are passed to the client. The number of new cases each day is calculated by subtracting the current day's total cases from yesterday's total cases (the first day is the same since all cases are new cases). This data is plotted on a line graph with Chart.js. When a new state is selected from the dropdown, the existing canvas containing the chart is deleted and recreated so that a new chart can be loaded. There is a slight delay between clicking the state on the dropdown and the chart loading due to the function that sends the state's records to the client.

The interactive plot can be reached with the URL "/" or "/chart". There is a button at the top that directs the user to the interactive map.

# Interactive Map
The interactive map uses D3 to display the death rate of all states. Each state and its total death rate is plotted on a map with D3 using GeoJSON coordinates. There are 5 colors on the legend/map that correspond with how high the death rate is for each state. Hovering over each state will reveal a tooltip with the name of the state and its death rate.

### Legend
x <= 0.005 : light yellow; 0.005 < x <= 0.008 : yellow; 0.08 < x <= 0.011 : orange; 0.011 < x <= 0.014 : red; x > 0.014 : dark red

The interactive map can be reached with the URL "/map". There is a button at the top that directs the user to the interactive chart.
