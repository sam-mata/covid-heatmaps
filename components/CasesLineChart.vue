<script setup lang="ts">
import * as Plot from "@observablehq/plot";
import PlotFigure from "../PlotFigure.js";
import { format } from "d3-format";
import * as data from "../helpers/CountryDataHelper.js"

const props = defineProps({
  country_code: String,
  selectedFeature: String,
})

let chartData = null;
if (props.selectedFeature === 'Deaths') {
  chartData = data.useAllTimeDeaths(props.country_code);
} else if (props.selectedFeature === 'Cases') {
  chartData = data.useAllTimeCases(props.country_code);
} else if (props.selectedFeature === 'Vaccinations') {
  chartData = data.useAllTimeVaccinations(props.country_code);
}

let date_range = [new Date('2020-01-01'), new Date(data.useLastDate(props.country_code))]

let chart = {
  width: 400,
  height: 300,
  x: {
    label: 'Date',
    domain: date_range,
  },
  y: {
    label: props.selectedFeature,
    domain: [0, Math.max(...chartData.map((d: any) => d[1]))],
    tickFormat: format(".2s"),
  },
  marks: [
    Plot.line(chartData, {
      curve: 'catmull-rom-open',
      stroke: props.selectedFeature === 'Deaths' ? '#9d174d' :
        props.selectedFeature === 'Cases' ? '#ca8a04' : '#0369a1',
      strokeWidth: 2,
    }),
    Plot.gridY({
      stroke: 'grey',
      strokeDasharray: "2,5",
      strokeOpacity: 0.50,
    }),
  ],
}
</script>

<template>
  <div v-if="chartData.length > 0">
    <h1 class="text-xl font-bold text-center font-open-sans">{{ selectedFeature }} Over Time</h1>
    <PlotFigure :options="chart" />
  </div>
  <p v-else class="text-lg">⚠️ No data available</p>
</template>