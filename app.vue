<script setup>
import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure.js";
import penguins from "./data/penguins.json";
import "./app.css";

const features = ['Deaths', 'Vaccinations', 'Cases'], feature = ref(features[0]);
const range = ref({ start: new Date(2020, 0, 1), end: new Date(2023, 11, 31), });
</script>

<template>
  <UContainer>
    <UCard class="h-screen">

      <!-- Header -->
      <template #header>
        <h1 class="text-7xl font-bold text-center py-6 font-open-sans">
          Covid-19 Visualiser
        </h1>
      </template>

      <!-- Body -->
      <UCardBody>
        <div class="flex">

          <!-- Map Settings -->
          <div class="w-1/4">
            <h2 class="font-bold text-3xl py-4 text-center font-baloo">Settings</h2>

            <!-- Feature Selection -->
            <div class="flex items-center">
              <UIcon name="i-heroicons-check-circle-solid" class="pr-6" />
              <h3 class="py-2 font-semibold pr-4 font-open-sans">Feature : </h3>
              <USelect v-model="feature" :options="features" />
            </div>

            <!-- Divider -->
            <UDivider class="py-4" />

            <!-- Date Range Selection -->
            <div class="flex items-center">
              <UIcon name="i-heroicons-calendar-days-16-solid" class="pr-6" />
              <h3 class="py-2 font-semibold font-open-sans">Date Range : </h3>
            </div>
            <VDatePicker v-model.range="range" mode="date" is-dark="system" color="yellow" />
          </div>

          <UDivider orientation="vertical" class="px-4" />

          <!-- Map -->
          <div>
            <h2 class="font-bold text-3xl py-2 text-center font-baloo">Map</h2>
            <!-- Plot-->
            <div class=" mx-auto w-fit p-4">
              <WorldMap />
            </div>
          </div>

        </div>
      </UCardBody>

      <!-- Footer -->
      <template #footer>
        <p class="pt-3 font-baloo">
          All work completed by
          <a href="https://github.com/zoepicone">Zoe Picone</a>, <a href="https://github.com/nathanbridgeearney">Nathan
            Bridge-Earney</a> , and <a href="https://github.com/sam-mata">Sam Mata</a>.
        </p>
        <p class="pt-1 font-baloo">
          Project code available <a href="https://github.com/sam-mata/covid-visualiser">here
          </a>.
        </p>
      </template>
    </UCard>
  </UContainer>
</template>
