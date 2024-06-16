import json

with open('cleaned_data.json', 'r') as json_file:
    country_data = json.load(json_file)

json_countries = {country_data[code]['location'] for code in country_data}

with open('data.js', 'r') as file:
    content = file.read()

json_start = content.find('{')
json_end = content.rfind('}') + 1
geojson_data = json.loads(content[json_start:json_end])

geojson_countries = {feature['properties']['ADMIN'] for feature in geojson_data['features']}

missing_in_geojson = json_countries - geojson_countries

extra_in_geojson = geojson_countries - json_countries

