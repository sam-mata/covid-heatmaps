import data from "../data/cleaned_data.json"

export function useCountryData(country_code) {
    return data[country_code].data
}

export function usePopForCountry(country_code) {
  return data[country_code].population
}

export function useAllTimeCases(country_code) {
  // format as [[date, cases], ...]
  let time_cases = useCountryData(country_code).map((d) => [d.date, d.total_cases])
  // drop elements with null values for cases
  return time_cases.filter((d) => d[1] != null)
}

export function useLastDate(country_code) {
  let time_cases = useAllTimeCases(country_code)
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
  let firstCase = time_cases.findIndex((d) => d[0] === start_date)
  let lastCase = time_cases.findIndex((d) => d[0] === end_date)

  return lastCase[1] - firstCase[1]
}