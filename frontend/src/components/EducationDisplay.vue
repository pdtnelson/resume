<script setup lang="ts">
import type { Education } from '@/domain/types.ts'

const { education } = defineProps<{ education: Education }>()
</script>

<template>
  <h2 class="text-base font-bold sm:text-xl sm:tracking-tight mb-1">{{ education.school }}, {{ education.city }} {{ education.state }}</h2>
  <h2 class="text-base sm:text-xl sm:tracking-tight mb-1">{{ education.description }}</h2>
</template>

<style scoped>

</style>
