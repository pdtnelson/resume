<script setup lang="ts">
import { inject, onBeforeMount, ref } from 'vue'
import type HttpClient from '@/http/http-client'
import type { PagedResponse, Profile, Resume } from '@/domain/types.ts'
import { useRoute } from 'vue-router'
import Hero from "@/components/Hero.vue";
import SkillsDisplay from "@/components/SkillsDisplay.vue";

const http: HttpClient = inject('http')!
const route = useRoute()
const default_uuid = import.meta.env.VITE_DEFAULT_PROFILE_UUID
const profile = ref<Profile>()

const getProfileTrackingId = () => {
  const { utm_id } = route.query
  return utm_id ? utm_id : default_uuid
}

const fetchData = async () => {
  try {
    const response = await http.client.get<PagedResponse<Profile>>(`/profiles?tracking_uuid=${getProfileTrackingId()}`)
    profile.value = response.data.data[0]
  } catch (e) {
    console.error(e)
  }
}

onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <Hero />
  <main class="container mx-auto mb-auto px-4 sm:px-6 lg:px-8">
    <section class="profile-intro-card relative z-10 -mt-32 p-10 bg-white rounded-3xl">
      <div class="flex justify-center -mt-20 sm:-mt-24 mb-6">
        <img src="/profile.jpeg"
             alt="Peter Nelson's Professional Photo"
             class="w-36 h-36 sm:w-48 sm:h-48 rounded-full object-cover border-4 border-white shadow-lg ring-4 ring-indigo-300 ring-opacity-70">
      </div>
      <p class="text-lg sm:text-xl text-gray-700 max-w-3xl mx-auto leading-relaxed mb-5">
        Over the past 16 years, I've gained experience in a wide variety of technical environments
        ranging from small startups just making their mark to large corporations that are household names.
        My approach has always been informed by my start in educational technology and my decisions are
        always made with careful analysis of the problem at hand. This allows me to go beyond buzzwords
        and build systems and solutions that address the exact needs of any organization.
      </p>
      <p class="text-lg sm:text-xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
        Skilled in Python, TypeScript, PHP, and Java. Experienced with
        AWS, Azure, GCP, Docker, Microservices, and RESTful development.
      </p>
    </section>
    <section id="links" class="grid grid-cols-1 md:grid-cols-3 gap-8 py-12">
      <RouterLink :to="{ name: 'resume' }" class="block">
        <div class="bg-white rounded-xl shadow-lg p-7 flex flex-col items-center text-center h-full transform hover:scale-105 transition-transform duration-300 ease-in-out hover:shadow-2xl border-b-4 border-gray-800">
          <svg class="w-16 h-16 text-gray-800 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">My Resume</h3>
          <p class="text-gray-700 mb-4">Take a look at my resume for a detailed look at my qualifications and experience.</p>
          <span class="text-blue-600 font-semibold hover:text-blue-800">View Resume &rarr;</span>
        </div>
      </RouterLink>
      <a href="https://github.com/pdtnelson" target="_blank" class="block">
        <div class="bg-white rounded-xl shadow-lg p-7 flex flex-col items-center text-center h-full transform hover:scale-105 transition-transform duration-300 ease-in-out hover:shadow-2xl border-b-4 border-gray-800">
          <svg class="w-16 h-16 text-gray-800 mb-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.499.09.679-.217.679-.481 0-.237-.008-.865-.013-1.7c-2.782.602-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.614.069-.601.069-.601 1.004.07 1.531 1.032 1.531 1.032.892 1.529 2.341 1.085 2.91.829.091-.645.356-1.085.654-1.334-2.22-.253-4.555-1.113-4.555-4.93 0-1.09.39-1.986 1.029-2.677-.103-.253-.446-1.268.099-2.648 0 0 .84-.27 2.75 1.021A9.582 9.582 0 0112 6.844c.85.004 1.701.114 2.503.333 1.909-1.291 2.747-1.021 2.747-1.021.546 1.38.202 2.395.099 2.648.64.691 1.028 1.587 1.028 2.677 0 3.827-2.339 4.673-4.566 4.92.359.307.678.915.678 1.846 0 1.335-.012 2.41-.012 2.727 0 .267.179.577.688.48C19.137 20.19 22 16.435 22 12.017 22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
          </svg>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">GitHub Profile</h3>
          <p class="text-gray-700 mb-4">Explore the code for this website and other things I've been working on in my free time.</p>
          <span class="text-blue-600 font-semibold hover:text-blue-800">Visit GitHub &rarr;</span>
        </div>
      </a>
      <RouterLink :to="{ name: 'blog' }" target="_blank" class="block">
        <div class="bg-white rounded-xl shadow-lg p-7 flex flex-col items-center text-center h-full transform hover:scale-105 transition-transform duration-300 ease-in-out hover:shadow-2xl border-b-4 border-gray-800">
          <svg class="w-16 h-16 text-gray-800 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.747 0-3.332.477-4.5 1.253"></path>
          </svg>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">My Blog</h3>
          <p class="text-gray-700 mb-4">Check out my blog to see what I'm interested in at the moment.</p>
          <span class="text-blue-600 font-semibold hover:text-blue-800">Visit Blog &rarr;</span>
        </div>
      </RouterLink>
    </section>
    <section class="bg-white rounded-2xl shadow-lg p-8 sm:p-10 md:p-12 mb-12">
      <SkillsDisplay title="My Expertise" />
    </section>
  </main>
</template>

<style lang="scss" scoped>
.profile-intro-card {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}
</style>
