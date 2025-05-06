<script setup lang="ts">
import type { Certification } from '@/domain/types.ts'

const { certification } = defineProps<{ certification: Certification }>()
</script>

<template>
  <h2 class="text-base font-bold sm:text-xl sm:tracking-tight mb-1">{{ certification.name }}</h2>
  <h2 class="text-base sm:text-xl sm:tracking-tight mb-1">{{ certification.issuer }}</h2>
  <h2 class="text-base sm:text-xl sm:tracking-tight mb-1" v-if="certification.certification_url">{{ certification.certification_url }}</h2>
</template>

<style scoped>

</style>
