<script setup lang="ts">
import "./app.css";

const features = [{ label: 'Deaths', }, { label: 'Cases', }, { label: 'Vaccinations', }]
const isOpen = ref(true)

</script>

<template>
  <div class="relative h-screen">
    <!-- Map (BACK) -->
    <WorldMap />

    <!-- Floating Overlay -->
    <div class="absolute inset-0 pointer-events-none">
      <!-- Top Div -->
      <div class="flex items-center justify-center w-full mt-10 pointer-events-auto lg:mt-20">
        <!-- Feature Selector-->
        <UTabs :items="features" :default-index="1" />

        <!-- Info Modal-->
        <div class="mb-2 ml-2 pointer-events-auto">
          <UButton icon="i-heroicons-information-circle" @click="isOpen = true" />
          <UModal v-model="isOpen">
            <StartModal />
          </UModal>
        </div>
      </div>

      <!-- Bottom Div -->
      <div class="absolute inset-x-0 w-3/5 mx-auto shadow-sm pointer-events-auto lg:w-1/2 bottom-40 lg:bottom-20">
        <Timescale />
      </div>
    </div>
  </div>
</template>