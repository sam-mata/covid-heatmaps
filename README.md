# Covid Visualiser

An interactive web app for visualising worldwide trends in Covid-19 data.

This project can be viewed live [here](https://covid-visualiser.vercel.app/).

---

## 1. Installation

```bash
pnpm install --shamefully-hoist
```

> [!NOTE]
> _The `--shamefully-hoist` flag **is** required, despite the name, as this flattens the node modules for production._

---

## 2. Usage

Starting the development server on [localhost](http://localhost:3000) can be done with:

```bash
pnpm run dev
```

> [!NOTE]
> _Nuxt will first have to initialise, which can take some time before the project structure is loaded and hot-reloading is available._

Running a production build instead can be done with:

```bash
pnpm run build
pnpm run preview
```

---

## 3. Dataset

This project uses a dataset provided by [OurWorldInData.org](OurWorldInData.org) which can be found [here](https://ourworldindata.org/coronavirus).
This dataset was initially preprocessed, particularly with the removal of several redundant tags that were out of scope for this project. The finalised dataset can be found [here](/data/cleaned_data.json), while the Jupyter notebook for preprocessing can be found [here](/data/preprocessing.ipynb).

The processed dataset can be understood in the following structure

-   Each JSON object is for one country, labelled by its country code _(e.g. `AFG` -> Afghanistan)_. This contains:
    -   `location` : The full name of the country
    -   `population` : The population of the country
    -   `data` : A sub-object that contains many fields:
        -   `date` : Date of update
        -   `total_cases` : Total cases as of that date
        -   `total_deaths` : Total deaths as of that date
        -   `people_vaccinated` : Total people vaccinate as of that date
        -   `stringency_index` : Index of government restrictions.
            ...

For a full list of fields, see the [official documentation of the original dataset](https://github.com/owid/covid-19-data/tree/master/public/data).

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
