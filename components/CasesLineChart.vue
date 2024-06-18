To display a loading message while fetching the data and then show either the graph or the "No data available" message
based on the data availability, you can modify the component as follows:
<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import * as Plot from "@observablehq/plot"
import PlotFigure from "../PlotFigure.js"
import { format } from "d3-format"
import * as helper from "../helpers/CountryDataHelper.js"

const props = defineProps({
  country_code: String,
  selectedFeature: String,
})

const chartData = ref<any[]>([])
const dateRange = ref<[Date, Date]>([new Date('2020-01-01'), new Date()])
const chart = ref<{
  width: number
  height: number
  x: { label: string; domain: [Date, Date] }
  y: { label: string; domain: [number, number]; tickFormat: (value: number) => string }
  marks: any[]
} | null>(null)
const isLoading = ref(true)

const featureLabel = computed(() => props.selectedFeature || "Unknown Feature")

const fetchChartData = async () => {
  isLoading.value = true

  let data
  if (props.selectedFeature === 'Deaths') {
    data = await helper.useAllTimeDeaths(props.country_code)
  } else if (props.selectedFeature === 'Cases') {
    data = await helper.useAllTimeCases(props.country_code)
  } else if (props.selectedFeature === 'Vaccinations') {
    data = await helper.useAllTimeVaccinations(props.country_code)
  }

  // Filter out invalid data points
  chartData.value = data.filter(d => d[1] !== undefined && d[1] !== null)

  const lastDate = await helper.useLastDate(props.country_code)
  dateRange.value = [new Date('2020-01-01'), new Date(lastDate)]

  if (chartData.value.length > 0) {
    chart.value = {
      width: 400,
      height: 300,
      x: {
        label: 'Date',
        domain: dateRange.value,
      },
      y: {
        label: featureLabel.value,
        domain: [0, Math.max(...chartData.value.map((d: any) => d[1]))],
        tickFormat: format(".2s"),
      },
      marks: [
        Plot.line(chartData.value, {
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
  }

  isLoading.value = false
}

onMounted(() => {
  fetchChartData()
})

watch(() => props.selectedFeature, fetchChartData) 
</script>
<template>
  <div v-if="isLoading">
    <p class="text-lg">Loading...</p>
  </div>
  <div v-else>
    <div v-if="chartData.length > 0">
      <h1 class="text-xl font-bold text-center font-open-sans">{{ selectedFeature }} Over Time</h1>
      <PlotFigure v-if="chart" :options="chart" />
    </div>
    <p v-else class="text-lg">⚠️ No data available</p>
  </div>
</template>