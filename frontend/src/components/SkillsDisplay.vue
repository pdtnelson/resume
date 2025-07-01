<script setup lang="ts">
import { inject, onMounted, ref } from 'vue'
import HttpClient from '@/http/http-client.ts'
import type { Resume } from '@/domain/types.ts'

const http: HttpClient = inject('http')!
const { title } = defineProps<{ title: string }>()
const skills = ref<string[]>()

const fetchData = async () => {
  try {
    const response = await http.client.get<Resume>(`/resume?revision=0`)
    skills.value = response.data.skills
  } catch (e) {
    console.error(e)
  }
}

onMounted(() => {
  fetchData()
})
</script>

<template>
  <h2 class="text-3xl sm:text-4xl font-extrabold text-gray-900 mb-8 text-center">
    {{ title }}
  </h2>
  <div class="flex flex-wrap justify-center gap-4">
    <span class="skill-badge inline-block py-2 px-4 rounded-full mr-3 mb-3 font-semibold
    text-[0.9rem] transition transform delay-200 ease-in-out hover:-translate-y-0.5 hover:scale-105
    bg-indigo-100 text-indigo-800"
    v-for="skill in skills">
      {{ skill }}
    </span>
  </div>
</template>

<style scoped></style>
