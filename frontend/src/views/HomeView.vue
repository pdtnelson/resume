<script setup lang="ts">
import { inject, onBeforeMount, ref } from 'vue'
import type HttpClient from '@/http/http-client'
import type { PagedResponse, Profile } from '@/domain/types.ts'
import { useRoute } from 'vue-router'

const http: HttpClient = inject('http')!
const route = useRoute()
const profile = ref<Profile>()
async function fetchData() {
  try {

    const response = await http.client.get<PagedResponse<Profile>>(`/profiles?tracking_uuid=${getProfileTrackingId()}`)
    profile.value = response.data.data[0]
  } catch (e) {
    console.error(e)
  }
}

const getProfileTrackingId = () => {
  const { utm_id } = route.query
  return utm_id ? utm_id : 'bb63c1de-161e-40ce-a202-b15bde733a61'
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
