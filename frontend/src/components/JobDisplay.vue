<script setup lang="ts">
import type { Job } from '@/domain/types.ts'

const { job } = defineProps<{job: Job}>()
</script>

<template>
  <div class="w-full text-black">
    <h1>{{ job.title }}</h1>
    <h2>{{ job.start_date }} - {{ job.end_date }}</h2>
    <p v-html="job.description"></p>
  </div>
</template>

<style scoped>

</style>
