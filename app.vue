<script setup lang="ts">
import "./app.css";

const features = [{ label: 'Deaths', }, { label: 'Cases', }, { label: 'Vaccinations', }]
const isOpen = ref(true)
const mapStyle = ref('light-v10')
const selectedFeatureIndex = ref(1) // Add this line to define selectedFeatureIndex

const toggleMapStyle = () => {
  mapStyle.value = mapStyle.value === 'light-v10' ? 'light-v11' : 'light-v10'
}
</script>

<template>
  <div class="relative h-screen">
    <!-- Map (BACK) -->
    <WorldMap :selected-feature="features[selectedFeatureIndex].label" :map-style="mapStyle" />

    <!-- Floating Overlay -->
    <div class="absolute inset-0 pointer-events-none">
      <!-- Top Div -->
      <div class="flex items-center justify-center mx-auto mt-10 space-x-2 pointer-events-auto lg:mt-20">
        <!-- Map Style Toggle -->
        <div class="mb-2 ml-2 pointer-events-auto">
          <UButton :icon="mapStyle === 'light-v10' ? 'i-heroicons-globe-alt' : 'i-heroicons-map'"
            @click="toggleMapStyle" />
        </div>

        <!-- Feature Selector-->
        <UTabs :items="features" :default-index="1" @change="selectedFeatureIndex = $event" />

        <!-- Info Modal-->
        <div class="mb-2 pointer-events-auto">
          <UButton icon="i-heroicons-information-circle" @click="isOpen = true" />
          <UModal v-model="isOpen">
            <StartModal />
          </UModal>
        </div>
      </div>
    </div>
  </div>
</template>

<!-- Bottom Div -->
<!-- <div class="absolute inset-x-0 w-3/5 mx-auto shadow-sm pointer-events-auto lg:w-1/2 bottom-40 lg:bottom-20">
        <Timescale />
      </div> -->