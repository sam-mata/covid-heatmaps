<script setup lang="ts">
import * as Plot from "@observablehq/plot";
import PlotFigure from "../PlotFigure.js";
import world from "../data/countries-110m.json"
import * as topojson from "topojson-client"

let countries = topojson.feature(world, world.objects.countries)
let options_hash = {
  marginTop: 0,
  marginBottom: 0,
  marginLeft: 0,
  marginRight: 0,
  width: 1920,
  projection: {
    type: 'mercator',
  },
  marks: [
    Plot.geo(countries, {
      fill: (d) => d.properties.name === 'United States of America'
    })
  ]
}
</script>

<template>
  <PlotFigure :options="options_hash" />
</template>