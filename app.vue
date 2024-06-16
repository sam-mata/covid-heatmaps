<script setup lang="ts">
import "./app.css";

const features = [{ label: 'Deaths', }, { label: 'Cases', }, { label: 'Vaccinations', }]
const isOpen = ref(true)
const mapStyle = ref('');
const selectedFeatureIndex = ref(1) // Add this line to define selectedFeatureIndex

const toggleMapStyle = () => {
  const currentStyle = mapStyle.value;
  const [theme, version] = currentStyle.split('-');
  const newVersion = version === 'v10' ? 'v11' : 'v10';
  mapStyle.value = `${theme}-${newVersion}`;
};

onMounted(() => {
  const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = prefersDarkMode ? 'dark' : 'light';
  mapStyle.value = `${theme}-v10`;
});
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
        <div class="mb-2 pointer-events-auto">
          <UButton :icon="mapStyle.includes('v10') ? 'i-heroicons-globe-alt' : 'i-heroicons-map'"
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