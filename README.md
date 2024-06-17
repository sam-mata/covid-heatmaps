# Covid Visualiser

An interactive web app for visualising worldwide trends in Covid-19 data.

This project can be viewed live [online](https://covid-visualiser.vercel.app/).

---

## 1. Installation

```bash
pnpm install --shamefully-hoist
```

> [!NOTE]
> _The `--shamefully-hoist` flag **is** required._

---

## 2. Usage

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

## 3. Dataset

This project uses a subset of the publicly available ["Data on COVID-19"](https://github.com/owid/covid-19-data/tree/master/public/data) dataset made by [Our World in Data](https://ourworldindata.org/coronavirus). Specifically, three measures are derived:

1.  `total_cases` - The total number of cases for a given country.
2.  `people_vaccinated` - The total number of people who recieved at least one dose in a given country.
3.  `total_deaths` - The total count of deaths attributed to Covid-19 in a given country.

This was then merged into the properties of each country in the publicly available [`geo-countries`](https://github.com/datasets/geo-countries) GEOJSON map sourced from [Natural Earth](https://www.naturalearthdata.com/) data.

---

## 4. Tools

| **TOOL**          | **USAGE**          | **DOCS**                                                   |
| ----------------- | ------------------ | ---------------------------------------------------------- |
| `Vercel`          | Hosting            | [docs](https://vercel.com/docs)                            |
| `Nuxt`            | Framework          | [docs](https://nuxt.com/docs/getting-started/introduction) |
| `Vue`             | JS Framework       | [docs](https://vuejs.org/guide/introduction.html)          |
| `TailwindCSS`     | Styling            | [docs](https://tailwindcss.com/docs/utility-first)         |
| `Nuxt UI`         | UI Components      | [docs](https://ui.nuxt.com/getting-started)                |
| `Observable Plot` | Data Visualisation | [docs](https://observablehq.com/plot/)                     |

---

## 5. Authorship

All work completed by [Zoe Picone](https://github.com/zoepicone), [Nathan Bridge-Earney](https://github.com/nathanbridgeearney), and [Sam Mata](https://github.com/sam-mata) in submission for SWEN422.
