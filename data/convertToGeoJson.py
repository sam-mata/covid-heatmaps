import json
from collections import OrderedDict

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

        last_entry = details['data'][-1] if details['data'] else {}
        last_valid_values = {
            'total_deaths': None,
            'total_cases': None,
            'stringency_index': None,
            'people_vaccinated': None,
            'total_tests': None
        }

        for entry in reversed(details['data']):
            for key in last_valid_values:
                if last_valid_values[key] is None and key in entry:
                    last_valid_values[key] = entry[key]

        data_add[code] = {
            'data': details['data'],
            'population': details.get('population'),
            'location': location,
            'last_known_values': last_valid_values
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
            updated_properties = OrderedDict()
            updated_properties.update(data_add[code])
            if 'last_known_values' in updated_properties:
                del updated_properties['last_known_values']
            updated_properties.update(data_add[code]['last_known_values'])
            if 'location' in updated_properties:
                del updated_properties['location']

            data_property = updated_properties.pop('data')
            updated_properties['data'] = data_property
            feature['properties'].update(updated_properties)
            break

updated_geojson = json.dumps(geojson)
updated_js = f"export default {updated_geojson};"

with open('data.js', 'w') as output_file:
    output_file.write(updated_js)

print("Updated data.js")
