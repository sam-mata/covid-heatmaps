# Covid Visualiser

An interactive web app for visualising worldwide trends in Covid-19 data.

This project can be viewed live [online](https://covid-visualiser.vercel.app/).

---

## 1. Gallery
<img src="https://github.com/sam-mata/covid-visualiser/assets/49130157/af3265b3-4dcd-4dad-af0d-9393d6b3302b" width="23%"></img> <img src="https://github.com/sam-mata/covid-visualiser/assets/49130157/b15464a3-6153-4daf-a0db-75ab00ea5c7a" width="23%"></img> <img src="https://github.com/sam-mata/covid-visualiser/assets/49130157/40cf0934-3675-4011-aee2-c8854f30ecfd" width="23%"></img> <img src="https://github.com/sam-mata/covid-visualiser/assets/49130157/10ae5871-29aa-4aae-a66c-6d8fbe369dc4" width="23%"></img> 


---

## 2. Installation

This project utilizes several dependencies, which can be installed with:

```bash
pnpm install --shamefully-hoist
```

> [!NOTE]
> _The `--shamefully-hoist` flag **is** required._

---

## 3. Usage

Starting the development server on [localhost](http://localhost:3000) can be done with:

```bash
pnpm run dev
```

> [!NOTE]
> _Nuxt will first have to initialise, which can take some time (~20 seconds) before the project structure is loaded and hot-reloading is available._

Running a production build instead can be done with:

```bash
pnpm run build
pnpm run preview
```

---

## 4. Dataset

This project uses a subset of the publicly available ["Data on COVID-19"](https://github.com/owid/covid-19-data/tree/master/public/data) dataset made by [Our World in Data](https://ourworldindata.org/coronavirus). Specifically, three measures are derived:

1.  `total_cases` - The total number of cases for a given country.
2.  `people_vaccinated` - The total number of people who recieved at least one dose in a given country.
3.  `total_deaths` - The total count of deaths attributed to Covid-19 in a given country.

This was then merged into the properties of each country in the publicly available [`geo-countries`](https://github.com/datasets/geo-countries) GEOJSON map sourced from [Natural Earth](https://www.naturalearthdata.com/) data.

---

## 5. Tools

| **TOOL**          | **USAGE**          | **DOCS**                                                   |
| ----------------- | ------------------ | ---------------------------------------------------------- |
| `Vercel`          | Hosting            | [docs](https://vercel.com/docs)                            |
| `Nuxt`            | Framework          | [docs](https://nuxt.com/docs/getting-started/introduction) |
| `Vue`             | JS Framework       | [docs](https://vuejs.org/guide/introduction.html)          |
| `TailwindCSS`     | Styling            | [docs](https://tailwindcss.com/docs/utility-first)         |
| `Nuxt UI`         | UI Components      | [docs](https://ui.nuxt.com/getting-started)                |
| `Observable Plot` | Data Visualisation | [docs](https://observablehq.com/plot/)                     |

---

## 6. Authorship

All work completed by [Zoe Picone](https://github.com/zoepicone), [Nathan Bridge-Earney](https://github.com/nathanbridgeearney), and [Sam Mata](https://github.com/sam-mata) in submission for SWEN422.
