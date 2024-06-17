const fetchData = async () => {
  try {
      const response = await fetch('data.json');
      if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Fetch operation:', error);
      return null;
  }
};


export async function useCountryData(country_code) {
  const data = await fetchData();
  if (!data) return [];

  const country = data.features.find(d => d.properties.ISO_A3 === country_code);
  return country?.properties.data || [];
}


export async function useAllTimeDeaths(country_code) {
  const countryData = await useCountryData(country_code);
  return countryData.map(entry => [new Date(entry.date), entry.total_deaths]);
}


export async function useAllTimeCases(country_code) {
  const countryData = await useCountryData(country_code);
  return countryData.map(entry => [new Date(entry.date), entry.total_cases]);
}

export async function useAllTimeVaccinations(country_code) {
  const countryData = await useCountryData(country_code);
  return countryData.map(entry => [new Date(entry.date), entry.people_vaccinated]);
}

export async function useLastDate(country_code) {
  const countryData = await useCountryData(country_code);
  const lastEntry = countryData[countryData.length - 1];
  return lastEntry ? lastEntry.date : '2020-01-01';
}
