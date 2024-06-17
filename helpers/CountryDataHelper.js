import data from "../public/data.json"

export function useCountryData(country_code) {
  let country_data = data.features.find((d) => d.properties.ISO_A3 === country_code).properties.data
  if (country_data === undefined) {
    return []
  }
  return country_data
}

export function usePopForCountry(country_code) {
  let pop = data.features.find((d) => d.properties.ISO_A3 === country_code).properties.population
  if (pop === undefined) {
    return null
  }
  return pop
}
export function useAllTimeDeaths(country_code) {
  let time_deaths = useCountryData(country_code).map((d) => [d.date, d.total_deaths]);
  return time_deaths.filter((d) => d[1] != null);
}

export function useAllTimeCases(country_code) {
  let time_cases = useCountryData(country_code).map((d) => [d.date, d.total_cases]);
  return time_cases.filter((d) => d[1] != null);
}

export function useAllTimeVaccinations(country_code) {
  let time_vaccinations = useCountryData(country_code).map((d) => [d.date, d.people_vaccinated]);
  return time_vaccinations.filter((d) => d[1] != null);
}

export function useLastDate(country_code) {
  let time_cases = useAllTimeCases(country_code)
  if (time_cases.length === 0) {
    return []
  }
  return time_cases[time_cases.length - 1][0]
}

export function useCasesRange(country_code, start_date, end_date) {
  // if start date and end date are Date objects, convert to string
  if (start_date instanceof Date) {
    start_date = start_date.toISOString().split("T")[0]
  }
  if (end_date instanceof Date) {
    end_date = end_date.toISOString().split("T")[0]
  }

  let time_cases = useAllTimeCases(country_code)
  if (time_cases.length === 0) {
    return null
  }

  let firstCase = time_cases.findIndex((d) => d[0] === start_date)
  let lastCase = time_cases.findIndex((d) => d[0] === end_date)

  return lastCase[1] - firstCase[1]
}