<script setup>
import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure.js";
import penguins from "./data/penguins.json";
const features = ['Deaths', 'Vaccinations', 'Cases'], feature = ref(features[0]);

import { ref } from 'vue';

const range = ref({
  start: new Date(2020, 0, 6),
  end: new Date(2020, 0, 10),
});
</script>

<template>
  <UContainer>
    <UCard>
      <template #header>
        <h1 class="text-6xl">
          Covid-19 Visualiser
        </h1>
      </template>
      <UCardBody>
        <div class="flex">
          <div class="w-1/4">
            <h2 class="font-extrabold text-3xl py-2">Map Settings</h2>
            <h3 class="py-2 font-semibold">Mapping:</h3>
            <USelect v-model="feature" :options="features" />
            <UDivider class="py-4" />
            <h3 class="py-2 font-semibold">Date Range:</h3>
            <VDatePicker v-model.range="range" mode="date" />
          </div>
          <UDivider orientation="vertical" class="px-4" />
          <div>
            <h2 class="font-extrabold text-3xl py-2">Map</h2>
            <div class=" mx-auto w-fit p-4">
              <WorldMap />
            </div>
          </div>
        </div>
      </UCardBody>
      <template #footer>
        <p>
          All work completed by Zoe Picone, Nathan Bridge-Earney, and Sam Mata.
        </p>
        <p>
          Project code available <ULink href="https://github.com/sam-mata/covid-visualiser">here</ULink>.
        </p>
      </template>
    </UCard>
  </UContainer>
</template>
