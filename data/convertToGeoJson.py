import json

name_mapping = {
    "Congo": "Republic of Congo",
    "Democratic Republic of Congo": "Democratic Republic of the Congo",
    "United States": "United States of America",
    "Czechia": "Czech Republic",
    "Serbia": "Republic of Serbia",
    "North Macedonia": "Macedonia",
    "Greece": "Greece",
    "Turkmenistan": "Turkmenistan",
    "Cote d'Ivoire": "Ivory Coast",
    "Guinea-Bissau": "Guinea Bissau",
    "Tanzania": "United Republic of Tanzania",
    "Eswatini": "Swaziland"
}
with open('cleaned_data.json', 'r') as json_file:
    country_data = json.load(json_file)

data_add = {}
for code, details in country_data.items():
    if 'data' in details:
        location = name_mapping.get(details['location'], details['location'])
        data_add[code] = {
            'data': details['data'],
            'population': details.get('population'),
            'location': location
        }

with open('countries.js', 'r') as file:
    content = file.read()

start = content.find('{')
end = content.rfind('}') + 1
geojson = json.loads(content[start:end])

for feature in geojson['features']:
    country_name = feature['properties']['ADMIN']
    for code in data_add:
        if data_add[code]['location'] == country_name:
            feature['properties'].update(data_add[code])
            break

updated_geojson = json.dumps(geojson)
updated_js = f"export default {updated_geojson};"

with open('data.js', 'w') as output_file:
    output_file.write(updated_js)

