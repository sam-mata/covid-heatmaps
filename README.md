# Covid Visualiser

An interactive web app for visualising worldwide trends in Covid-19 data.

This project can be viewed live [here](https://covid-visualiser.vercel.app/).

---

## 1. Installation

```bash
pnpm install --shamefully-hoist
```

> [!NOTE] > _The `--shamefully-hoist` flag **is** required, despite the name, as this flattens the node modules for production._

---

## 2. Usage

Starting the development server on [localhost](http://localhost:3000) can be done with:

```bash
pnpm run dev
```

> [!NOTE] > _Nuxt will first have to initialise, which can take some time before the project structure is loaded and hot-reloading is available._

Running a production build instead can be done with:

```bash
pnpm run build
pnpm run preview
```

---

## 3. Dataset
Gathered From: https://github.com/owid/covid-19-data/tree/master/public/data

Edouard Mathieu, Hannah Ritchie, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Saloni Dattani, Diana Beltekian, Esteban Ortiz-Ospina and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]

| Metrics                     | Source                                                    | Accessed/Updated\*                                                          | Countries |
| --------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- | --------- |
| Vaccinations                | Official data collated by the Our World in Data team      | Daily                                                                       | 218       |
| Tests & positivity          | Official data collated by the Our World in Data team      | [No longer updated](https://github.com/owid/covid-19-data/discussions/2667) | 193       |
| Hospital & ICU              | Official data collated by the Our World in Data team      | Daily                                                                       | 46        |
| Confirmed cases             | WHO COVID-19 Data                                         | Daily                                                                       | 219       |
| Confirmed deaths            | WHO COVID-19 Data                                         | Daily                                                                       | 219       |
| Reproduction rate           | Arroyo-Marioli F, Bullano F, Kucinskas S, Rondón-Moreno C | Daily                                                                       | 196       |
| Policy responses            | Oxford COVID-19 Government Response Tracker               | Daily                                                                       | 185       |
| Other variables of interest | International organizations (UN, World Bank, OECD, IHME…) | Fixed                                                                       | 242       |
---
Removed certain tags as they are out of scope. Could be revised\
Removed Tags: \
"new_cases_smoothed", "new_deaths_smoothed", "new_cases_smoothed_per_million",
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
"handwashing_facilities", "hospital_beds_per_thousand", "life_expectancy", "human_development_index"

## 4. Tools

| **TOOL**          | **USAGE**          | **DOCS**                                                   |
| ----------------- | ------------------ | ---------------------------------------------------------- |
| `Vercel`          | Hosting            | [docs](https://vercel.com/docs)                            |
| `Nuxt`            | Framework          | [docs](https://nuxt.com/docs/getting-started/introduction) |
| `Vue`             | JS Framework       | [docs](https://vuejs.org/guide/introduction.html)          |
| `TailwindCSS`     | Styling            | [docs](https://tailwindcss.com/docs/utility-first)         |
| `Nuxt UI`         | UI Components      | [docs](https://ui.nuxt.com/getting-started)                |
| `D3`              | Data Visualisation | [docs](https://d3js.org/)                                  |
| `Observable Plot` | Data Visualisation | [docs](https://observablehq.com/plot/)                     |

---

## 5. Authorship

All work completed by Zoe Picone, Nathan Bridge-Earney, and Sam Mata in submission for SWEN422.
