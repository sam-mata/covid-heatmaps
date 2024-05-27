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
