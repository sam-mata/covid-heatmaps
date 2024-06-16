<script setup lang="ts">
import * as Plot from "@observablehq/plot";
import PlotFigure from "../PlotFigure.js";
import {format} from "d3-format";
import * as data from "../helpers/CountryDataHelper.js"

const props = defineProps({
  country_code: String,
})

let cases = data.useAllTimeCases(props.country_code)
let date_range = [new Date('2020-01-01'), new Date(data.useLastDate(props.country_code))]

let chart = {
  // Responsive width
  width: 400,
  height: 300,
  x: {
    label: 'Date',
    domain: date_range,
  },
  y: {
    label: 'Cases',
    domain: [0, Math.max(...cases.map((d: any) => d[1]))],
    tickFormat: format(".2s"),
  },
  marks: [
    Plot.line(cases, {
      // add smoothing
      curve: 'catmull-rom-open',
      stroke: 'black',
    })
  ]
}
</script>

<template>
  <PlotFigure v-if="cases.length > 0" :options="chart" />
  <p v-else>No cases found for country</p>
</template>

<style scoped>

</style>
