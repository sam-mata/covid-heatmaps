import json

with open('cleaned_data.json', 'r') as json_file:
    country_data = json.load(json_file)

data_add = {}
for code, details in country_data.items():
    if 'data' in details:
        data_add[code] = {
            'data': details['data'],
            'population': details.get('population')
        }

with open('countries.js', 'r') as file:
    content = file.read()

start = content.find('{')
end = content.rfind('}') + 1
geojson = json.loads(content[start:end])

for feature in geojson['features']:
    country_name = feature['properties']['ADMIN']
    for code in data_add:
        if country_data[code]['location'] == country_name:
            feature['properties'].update(data_add[code])
            break

updated_geojson = json.dumps(geojson)
updated_js = f"export default {updated_geojson};"

with open('data.js', 'w') as output_file:
    output_file.write(updated_js)


#%%
