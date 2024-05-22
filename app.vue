<script setup>
import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure.js";
import penguins from "./data/penguins.json";
import WorldMap from "~/components/WorldMap.ts";
</script>

<template>
  <div class="mx-auto w-fit py-24">
    <h1 class="text-5xl font-bold text-blue-700">Plot + Nuxt Works Bozos</h1>
    <PlotFigure :options="{
      marks: [
        Plot.dot(penguins, { x: 'culmen_length_mm', y: 'culmen_depth_mm' }),
      ],
    }" />
  </div>
</template>
