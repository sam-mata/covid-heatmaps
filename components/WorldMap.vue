<script setup lang="ts">
import * as Plot from "@observablehq/plot";
import PlotFigure from "../PlotFigure.js";
import {h} from "vue";
import world from "../data/countries-110m.json"
import * as topojson from "topojson-client"

let countries = topojson.feature(world, world.objects.countries)
</script>

<template>
  <PlotFigure :options="{
    height: 500,
    projection: 'equal-earth',
    marks: [
        Plot.geo(countries, {
            fill: (d) => d.properties.name === 'United States of America'
        })
    ]
  }" />
</template>

<style scoped>

</style>
