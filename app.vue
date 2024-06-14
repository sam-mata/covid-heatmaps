<script setup lang="ts">
import "./app.css";

const features = [{ label: 'Deaths', }, { label: 'Cases', }, { label: 'Vaccinations', }]
const isOpen = ref(true)

</script>

<template>
  <div class="relative h-screen">

    <!-- Map (BACK) -->
    <WorldMap />

    <!-- Overlay (FRONT) -->
    <!-- <div class="absolute inset-0 flex flex-col items-center justify-between"> -->

    <!-- Top Div -->
    <!-- <div class="flex items-center justify-center w-full mt-20"> -->

    <!-- Feature Selector-->
    <!-- <UTabs :items="features" :default-index="1" /> -->

    <!-- Info Modal-->
    <!-- <div class="absolute top-20 right-[28rem]">
          <UButton icon="i-heroicons-information-circle" @click="isOpen = true" />
          <UModal v-model="isOpen">
            <StartModal />
          </UModal>
        </div>
      </div> -->

    <!-- Bottom Div -->
    <!-- <div class="w-1/2 shadow-sm mb-28">
        <Timescale />
      </div> -->

    <!-- </div> -->

  </div>
</template>