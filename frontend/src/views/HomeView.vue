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
  <main class="flex flex-col flex-1 min-h-full -mt-16 mb-7">
    <div id="hero" class="flex flex-initial h-32 md:h-80"></div>
    <div id="profile-picture" class="flex items-center justify-center">
      <img class="rounded-full -mt-[125px]" src="https://placecats.com/250/250" alt="">
    </div>
    <div class="container mx-auto mt-5 px-4 sm:px-6 lg:px-8">
      <div>
        <p class="text-lg">
          Same shaman banjo, you probably haven't heard of them fingerstache salvia waistcoat.
          Poutine glossier gochujang air plant gluten-free, put a bird on it biodiesel VHS aesthetic dreamcatcher activated charcoal.
          Beard sriracha ascot, williamsburg paleo mlkshk taxidermy.
          Jawn roof party flexitarian you probably haven't heard of them la croix
          microdosing kombucha artisan gochujang hella. Kickstarter crucifix palo santo, polaroid XOXO
          fam portland tilde hexagon sus fashion axe Brooklyn paleo freegan bespoke. Tacos celiac tbh,
          hexagon hoodie man bun solarpunk DIY taiyaki.
          <br/>
          <br/>
          Microdosing aesthetic hell of hella quinoa pitchfork put a bird on it pour-over hashtag blue
          bottle squid tonx keytar roof party slow-carb. Same selvage jianbing woke schlitz kogi
          typewriter solarpunk jean shorts. Authentic meggings gluten-free flannel drinking vinegar
          four dollar toast. Subway tile seitan shaman distillery tousled occupy marfa poutine kogi
          organic artisan franzen solarpunk JOMO ascot. Listicle glossier everyday carry selfies DSA
          letterpress. Asymmetrical tote bag gorpcore, schlitz tbh adaptogen venmo sriracha selvage
          PBR&B slow-carb grailed.
        </p>
      </div>
      <div id="showcase" class="h-96 mt-5 px=7 grid grid-cols-1 md:grid-cols-3 md:gap-5">
        <div class="flex flex-col justify-center items-center rounded-lg dark:bg-slate-600">
          <RouterLink :to="{ name: 'resume' }" class="text-white text-center">
            <DocumentTextIcon class="h-56 w-56"/>
            <p>View my Resume</p>
          </RouterLink>
        </div>
        <div class="flex flex-col justify-center items-center rounded-lg dark:bg-slate-600">
          <a href="https://github.com/pdtnelson" class="text-white text-center">
            <img class="h-56 w-56 pb-3" src="/github-mark-white.svg" alt="">
            <p>Check out my GitHub</p>
          </a>
        </div>
        <div class="flex flex-col justify-center items-center rounded-lg dark:bg-slate-600">
          <RouterLink :to="{ name: 'blog' }" class="text-white text-center">
            <BookOpenIcon class="h-56 w-56"/>
            <p>Read My Blog</p>
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
