<script setup lang="ts">
import type { Job } from '@/domain/types.ts'

const { job } = defineProps<{job: Job}>()
</script>

<template>
  <h2 class="text-base font-bold sm:text-xl sm:tracking-tight mb-1">{{ job.title}} - {{ job.company }}</h2>
  <h2 class="text-base sm:text-xl sm:tracking-tight mb-1">{{ job.start_date?.toLocaleString() }} - {{ job.end_date? job.end_date.toLocaleString() : 'Present'}}</h2>
  <div v-html="job.description" class="job-description ml-5"></div>
</template>

<style lang="scss">
.job-description {
  ul {
    list-style: disc;
  }
}
</style>
