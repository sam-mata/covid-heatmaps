<template>
    <!-- Component for selector sections-->
    <div class="flex items-center">
        <UIcon :name="`i-heroicons-${icon}`" class="pr-6" />
        <h3 class="py-2 font-semibold">{{ title }} :</h3>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

// Component props
const props = defineProps({
    title: {
        type: String,
        required: true,
    },
    icon: {
        type: String,
        required: true,
    },
});
</script>
