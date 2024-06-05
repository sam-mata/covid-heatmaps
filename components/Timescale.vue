<script>
import Slider from '@vueform/slider'

let covid_data_start_date = new Date(2020, 1, 1).getTime()
let covid_data_end_date = new Date(2023, 11, 31).getTime()

export default {
  components: {
    Slider,
  },
  data() {
    return {
      value: [covid_data_start_date, covid_data_end_date],
      min: covid_data_start_date,
      max: covid_data_end_date,
      step: 86400000,
      tooltipPosition: 'bottom',
      format: function (value) {
        // Convert time in milliseconds to a date string
        return new Date(value).toDateString()
      }
    }
  }
}
</script>

<template>
  <div>
    <Slider v-model="value" :min="min" :max="max" :step="step" :tooltipPosition="tooltipPosition" :format="format" />
  </div>
</template>

<style lang="scss">
  @import 'node_modules/@vueform/slider/themes/tailwind.scss';
</style>
