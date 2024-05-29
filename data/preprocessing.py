#%%
import json
#%%
def remove_redundant_dates(country_data):
    filtered_data = []
    previous_entry = None

    for entry in country_data:
        if previous_entry is None or any(
                key != 'date' and (key not in previous_entry or entry[key] != previous_entry[key])
                for key in entry
        ):
            filtered_data.append(entry)
        previous_entry = entry

    return filtered_data
#%%
def remove_specified_fields(data, fields_to_remove):
    if isinstance(data, dict):
        return {key: remove_specified_fields(value, fields_to_remove) for key, value in data.items() if key not in fields_to_remove}
    elif isinstance(data, list):
        return [remove_specified_fields(item, fields_to_remove) for item in data]
    else:
        return data
#%%
def remove_specified_countries(data, countries_to_remove):
    return {key: value for key, value in data.items() if key not in countries_to_remove}
#%%
fields_to_remove = {"new_cases_smoothed", "new_deaths_smoothed", "new_cases_smoothed_per_million",
                  "new_deaths_smoothed_per_million", "new_cases", "new_cases_per_million", "new_deaths",
                  "new_deaths_smoothed", "new_deaths_per_million", "new_deaths_smoothed_per_million",
                  "excess_mortality", "excess_mortality_cumulative", "excess_mortality_cumulative_absolute",
                  "excess_mortality_cumulative_per_million", "icu_patients", "icu_patients_per_million",
                  "hosp_patients", "hosp_patients_per_million", "weekly_icu_admissions",
                  "weekly_icu_admissions_per_million", "weekly_hosp_admissions", "weekly_hosp_admissions_per_million",
                  "reproduction_rate", "new_tests", "new_tests_per_thousand", "new_tests_smoothed",
                  "new_tests_smoothed_per_thousand", "positive_rate", "tests_per_case", "tests_units",
                  "total_vaccinations", "people_fully_vaccinated", "total_boosters", "new_vaccinations",
                  "new_vaccinations_smoothed", "total_vaccinations_per_hundred", "people_fully_vaccinated_per_hundred",
                  "total_boosters_per_hundred", "new_vaccinations_smoothed_per_million",
                  "new_people_vaccinated_smoothed", "new_people_vaccinated_smoothed_per_hundred", "population_density",
                  "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "extreme_poverty",
                  "cardiovasc_death_rate", "diabetes_prevalence", "female_smokers", "male_smokers",
                  "handwashing_facilities", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"}

countries_to_remove = {"OWID_AFR","OWID_ASI","OWID_ENG","OWID_EUR","OWID_EUN","OWID_HIC","OWID_KOS","OWID_LIC","OWID_LMC","OWID_NAM","OWID_CYN","OWID_NIR","OWID_OCE","OWID_SCT","OWID_SAM","OWID_UMC","OWID_WLS"}
#%%
with open('data.json', 'r') as input_file:
    json_data = json.load(input_file)

data_without_specified_countries = remove_specified_countries(json_data, countries_to_remove)
data_with_removed_fields = remove_specified_fields(data_without_specified_countries, fields_to_remove)

for country, country_data in data_with_removed_fields.items():
    if 'data' in country_data:
        country_data['data'] = remove_redundant_dates(country_data['data'])

with open('cleaned_data.json', 'w') as output_file:
    json.dump(data_with_removed_fields, output_file, indent=4)

print("Data cleaned and saved to cleaned_data.json.") 