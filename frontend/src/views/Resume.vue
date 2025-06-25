<script setup lang="ts">

import type HttpClient from '@/http/http-client.ts'
import { inject, onMounted, ref } from 'vue'
import type { PagedResponse, Resume } from '@/domain/types.ts'
import Card from '@/components/Card.vue'
import JobDisplay from '@/components/JobDisplay.vue'
import EducationDisplay from '@/components/EducationDisplay.vue'
import CertificationDisplay from '@/components/CertificationDisplay.vue'
import Timeline from '@/components/Timeline.vue'

const http = inject<HttpClient>('http')!
const resume = ref<Resume>()

const fetchData = async () => {
  try {
    const response = await http.client.get<PagedResponse<Resume>>('/resumes')
    resume.value = response.data.data[0]
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  fetchData()
})
</script>

<template>
  <header class="page-header text-white px-4 sm:px-6 lg:px-8">
    <div class="container mx-auto text-center py-8">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-2 drop-shadow-md">
        Professional Experience
      </h1>
      <p class="text-lg sm:text-xl font-light opacity-90 max-w-2xl mx-auto">
        A journey through my career in software engineering.
      </p>
    </div>
  </header>
  <main class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <Timeline :jobs="[]" />
  </main>
</template>

<style lang="scss">
</style>
