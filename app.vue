<script setup>
import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure.js";
import penguins from "./data/penguins.json";
import WorldMap from "~/components/WorldMap.ts";


const features = ['Deaths', 'Vaccinations', 'Cases'], feature = ref(features[0]);
const range = ref({ start: new Date(2020, 0, 1), end: new Date(2023, 11, 31), });
</script>

<template>
  <UContainer>
    <UCard class="h-screen">

      <!-- Header -->
      <template #header>
        <h1 class="text-6xl font-bold text-center py-6">
          Covid-19 Visualiser
        </h1>
      </template>

      <!-- Body -->
      <UCardBody>
        <div class="flex">

          <!-- Map Settings -->
          <div class="w-1/4">
            <h2 class="font-bold text-3xl py-2 text-center">Settings</h2>
            <!-- Feature Selection -->
            <SelectorSection title="Feature" icon="check-circle-solid" />
            <USelect v-model="feature" :options="features" />

            <UDivider class="py-4" />

            <!-- Date Range Selection -->
            <SelectorSection title="Date" icon="calendar-days-16-solid" />
            <VDatePicker v-model.range="range" mode="date" />
          </div>

          <UDivider orientation="vertical" class="px-4" />

          <!-- Map -->
          <div>
            <h2 class="font-bold text-3xl py-2 text-center">Map</h2>
            <!-- Plot-->
            <div class=" mx-auto w-fit p-4">
              <PlotFigure :options="{
                marks: [
                  Plot.dot(penguins, { x: 'culmen_length_mm', y: 'culmen_depth_mm' }),
                ],
              }" />
            </div>
          </div>

        </div>
      </UCardBody>

      <!-- Footer -->
      <template #footer>
        <p class="text-center pt-3">
          All work completed by Zoe Picone, Nathan Bridge-Earney, and Sam Mata.
        </p>
        <p class="text-center">
          Project code available <ULink href="https://github.com/sam-mata/covid-visualiser"
            class="underline underline-offset-2">here
          </ULink>.
        </p>
      </template>
    </UCard>
  </UContainer>
</template>
