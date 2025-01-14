import json
import csv

# open stations files
with open('stations.csv') as file:
    stations = list(csv.DictReader(file))

# open precipitation file
with open ('precipitation.json') as file:
    contents = json.load(file)

# define a dictionary to store information
precipitation_info = {}

for station in stations:
    # City data
    station_number = station['Station']
    state = station['State']
    city_name = station['Location']

    # create a list with the values of precipitation
    city_data = []
    for measurements in contents:
        if (measurements['station']) == station_number:
            city_data.append(measurements)

    # calculate total precipitation by month
    total_monthly_precipitation = {}

    #for values in seattle_data:
    for measurements in city_data:
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

    #store the results in the precipitation information dictionary
    precipitation_info[city_name] = {
            'station' : station_number,
            'state' : state,
            'total_monthly_precipitation' : list(total_monthly_precipitation.values()),
            'total_yearly_precipitation' : total_yearly_precipitation,
            'relative_monthly_precipitation' : list(relative_monthly_precipitation.values())
}
    
total_precipitation_all_stations = 0
# calculate relative yearly precipitation
for city_name, data in precipitation_info.items():
    # add to the total for all stations
    total_precipitation_all_stations += total_yearly_precipitation
    # divide total yearly precipitation of one city by the sum of the total yearly precipitation of all cities
    relative_yearly_precipitation = (data['total_yearly_precipitation'] / total_precipitation_all_stations)
    # Add the relative yearly precipitation to the dictionary
    precipitation_info[city_name]['relative_yearly_precipitation'] = relative_yearly_precipitation

#store the results in results.json file
with open('results.json','w') as file:
    json.dump(precipitation_info,file, indent=4)