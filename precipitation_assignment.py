import json
import csv

# open precipitation file
with open ('precipitation.json') as file:
    contents = json.load(file)

# Seatlle data
station_number = 'GHCND:USW00093814'
state = 'WA'
city_name = 'Seattle'

# create a list with the values of precipitation
seattle_data = []
for measurements in contents:
    if (measurements['station']) == station_number:
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

# difine a dictionary to store information
precipitation_info = {}

#store the results in the precipitation information dictionary
precipitation_info[city_name] = {
        'station' : station_number,
        'state' : state,
        'total_monthly_precipitation' : total_monthly_precipitation
}
#store the results in results.json file
with open('results.json','w') as file:
    json.dump(precipitation_info,file, indent=4)