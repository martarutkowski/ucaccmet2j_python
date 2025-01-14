import json
import csv

# open precipitation file
with open ('precipitation.json') as file:
    contents = json.load(file)

# Seatlle data
station_number = 'GHCND:US1WAKG0038'
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

# calculating total yearly precipitation
total_yearly_precipitation = sum(total_monthly_precipitation.values())

# calculating relative monthly precipitation
# creating a dictionary 
relative_monthly_precipitation = {}

for month, monthly_total in total_monthly_precipitation.items():
    relative_monthly_precipitation[month] = monthly_total/total_yearly_precipitation

# define a dictionary to store information
precipitation_info = {}

#store the results in the precipitation information dictionary
precipitation_info[city_name] = {
        'station' : station_number,
        'state' : state,
        'total_monthly_precipitation' : total_monthly_precipitation,
        'total_yearly_precipitation' : total_yearly_precipitation,
        'relative_monthly_precipitation' : relative_monthly_precipitation
}
#store the results in results.json file
with open('results.json','w') as file:
    json.dump(precipitation_info,file, indent=4)