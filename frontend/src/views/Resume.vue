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
  <main class="flex flex-1 flex-col min-h-full">
    <div class="text-right pr-7">
      <a href="/pdtnelson-resume.pdf">Prefer a PDF?</a>
    </div>
    <div class="flex flex-col min-h-full w-full mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8" v-if="resume">
      <div class="mb-5 text-center w-full">
        <h2 class="text-xl sm:truncate sm:text-3xl sm:tracking-tight mb-2 dark:text-gray-200">Skills</h2>
        <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2">
          <div v-for="(skill, index) in resume.skills" :key="index">
            <p class="text-base text-gray-200 font-semibold">{{ skill }}</p>
          </div>
        </div>
      </div>
      <div class="mb-5 text-center">
        <h2 class="text-xl sm:text-3xl sm:tracking-tight dark:text-gray-200">
          Experience
        </h2>
      </div>
      <Timeline :jobs="resume.jobs"/>
    </div>
  </main>
</template>

<style lang="scss">
</style>
