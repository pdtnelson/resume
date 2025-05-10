<script setup lang="ts">
import { inject, onBeforeMount, ref } from 'vue'
import type HttpClient from '@/http/http-client'
import type { PagedResponse, Profile } from '@/domain/types.ts'
import { useRoute } from 'vue-router'
import { BookOpenIcon, DocumentTextIcon } from '@heroicons/vue/24/solid'

const http: HttpClient = inject('http')!
const route = useRoute()
const default_uuid = import.meta.env.VITE_DEFAULT_PROFILE_UUID
const profile = ref<Profile>()
const targetedProfile = ref(true)
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
  return utm_id ? utm_id : default_uuid
}
onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <main class="flex flex-col flex-1 min-h-full -mt-16 mb-7 dark:text-neutral-300 bg-neutral-50 dark:bg-zinc-900 text-zinc-900">
    <div id="hero" class="flex flex-initial h-32 md:h-80 xl:h-96"></div>
    <div id="profile-picture" class="flex items-center justify-center">
      <img class="rounded-full -mt-[125px] h-64 w-64" src="/profile.jpeg" alt="">
    </div>
    <div class="container mx-auto mt-5 px-4 sm:px-6 lg:px-8">
      <div class="mb-8 xl:mb-16">
        <p class="font-extrabold text-3xl xl:text-4xl mb-2">I'm Peter.</p>
        <p class="font-bold text-2xl xl:text-3xl mb-3">Software Engineer. Security Enthusiast. Skier.</p>
        <p class="text-lg xl:text-xl font-semibold">
          I've been writing software and working on web projects since 2013 and have worked for small startups, household names and everything in between.
          I have extensive experience designing applications, architecting infrastructure, and engaging with project stakeholders.
          Code is a tool that I use to solve business problems and help organizations thrive on their way to achieving their goals.
          <span class="font-semibold" v-if="targetedProfile">You can get a better idea of my accomplishments and abilities via the links below. If you're interested in what you see, get in touch with me and we can talk about how I can
            contribute to your amazing company.</span>
        </p>
      </div>
      <div id="showcase" class="sm:h-72 xl:h-96  sm:mx-auto px=7 grid grid-cols-1 md:grid-cols-3 md:gap-8">
        <div class="flex flex-col justify-center items-center bg-white shadow-lg dark:shadow-md dark:shadow-white rounded">
          <RouterLink :to="{ name: 'resume' }" class="text-zinc-900 text-center">
            <DocumentTextIcon class="h-56 w-56"/>
            <p class="text-xl text-semibold">View my Resume</p>
          </RouterLink>
        </div>
        <div class="flex flex-col justify-center items-center bg-white shadow-lg dark:shadow-md dark:shadow-white rounded">
          <a href="https://github.com/pdtnelson" class="text-zinc-900 text-center">
            <img class="h-56 w-56 pb-3" src="/github-mark.svg" alt="">
            <p class="text-xl text-semibold">Check out my GitHub</p>
          </a>
        </div>
        <div class="flex flex-col justify-center items-center bg-white shadow-lg dark:shadow-md dark:shadow-white rounded">
          <RouterLink :to="{ name: 'blog' }" class="text-zinc-900 text-center">
            <BookOpenIcon class="h-56 w-56"/>
            <p class="text-xl text-semibold">Read My Blog</p>
          </RouterLink>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
#hero {
  background-image: url("/code_2.png");
}
</style>
