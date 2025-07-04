<script setup lang="ts">
import type HttpClient from '@/http/http-client.ts'
import { inject, onBeforeMount, ref } from 'vue'
import type { Resume } from '@/domain/types.ts'
import Timeline from '@/components/Timeline.vue'
import PageHeader from '@/components/PageHeader.vue'

const http = inject<HttpClient>('http')!
const resume = ref<Resume>()

const fetchData = async () => {
  try {
    const response = await http.client.get<Resume>('/resume')
    resume.value = response.data
  } catch (e) {
    console.log(e)
  }
}

onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <PageHeader title="Professional Experience" desc="A detailed look through my previous positions" />
  <main class="container mx-auto mb-auto px-4 sm:px-6 lg:px-8 py-12">
    <Timeline v-if="resume" :jobs="resume.jobs" />
  </main>
</template>

<style lang="scss">
</style>
