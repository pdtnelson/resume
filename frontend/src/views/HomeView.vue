<script setup lang="ts">
import { inject, onBeforeMount, ref } from 'vue'
import type HttpClient from '@/http/http-client'
import type { Profile } from '@/domain/types.ts'

const http: HttpClient = inject('http')!
const profile = ref<Profile>()
async function fetchData() {
  try {
    const response = await http.client.get<Profile>('/profiles/67909cf0a23641e6b4ff52a3')
    profile.value = response.data
  } catch (e) {
    console.error(e)
  }
}

onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <main class="w-full lg:w-4/5 px-2 lg:px-7 mx-auto">
    <div v-if="profile">
      <img class="h-fit w-fit float-left mr-7" :src="profile.profile_img_url" alt="Placeholder Cat">
      <p>{{ profile.text }}</p>
    </div>
  </main>
</template>
