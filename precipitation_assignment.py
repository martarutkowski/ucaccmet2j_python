import json
import csv

# open precipitation file
with open ('precipitation.json') as file:
    contents = json.load(file)

# station code of Seatlle
seattle_station = 'GHCND:USW00093814'

# create a list with the values of precipitation
seattle_data = []
for measurements in contents:
    if (measurements['station']) == seattle_station:
        seattle_data.append(measurements)

# calculate total precipitation by month
total_monthly_precipitation = {}

#for values in seattle_data:
for measurements in seattle_data:
    month = int(measurements['date'].split('-')[1]) #spliting the date, taking the months and make it an integer
    # add precipitation to the corresponding month
    if month in total_monthly_precipitation:
        total_monthly_precipitation[month] += measurements['value'] # add precipitation if month in the dictionary
    else:
        total_monthly_precipitation[month] = 0  # enter the month if not already in the dictionary

