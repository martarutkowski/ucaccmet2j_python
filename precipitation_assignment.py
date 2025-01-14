import json

# open precipitation file
with open ('precipitation.json') as file:
    contents = json.load(file)

# station code of Seatlle
seattle_station = 'GHCND:USW00093814'

# create a list with the values of precipitation
seattle_data = []
for measurements in contents:
    if (measurements['station']) == seattle_station:
        seattle_data.append(measurements['value'])



