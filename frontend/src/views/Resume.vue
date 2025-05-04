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
  <main class="flex flex-1 min-h-full">
    <div class="flex flex-col min-h-full w-full mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8" v-if="resume">
<!--      <div>-->
<!--        <p class="text-lg">-->
<!--          Same shaman banjo, you probably haven't heard of them fingerstache salvia waistcoat.-->
<!--          Poutine glossier gochujang air plant gluten-free, put a bird on it biodiesel VHS aesthetic dreamcatcher activated charcoal.-->
<!--          Beard sriracha ascot, williamsburg paleo mlkshk taxidermy.-->
<!--          Jawn roof party flexitarian you probably haven't heard of them la croix-->
<!--          microdosing kombucha artisan gochujang hella. Kickstarter crucifix palo santo, polaroid XOXO-->
<!--          fam portland tilde hexagon sus fashion axe Brooklyn paleo freegan bespoke. Tacos celiac tbh,-->
<!--          hexagon hoodie man bun solarpunk DIY taiyaki.-->
<!--          <br/>-->
<!--          <br/>-->
<!--          Microdosing aesthetic hell of hella quinoa pitchfork put a bird on it pour-over hashtag blue-->
<!--          bottle squid tonx keytar roof party slow-carb. Same selvage jianbing woke schlitz kogi-->
<!--          typewriter solarpunk jean shorts. Authentic meggings gluten-free flannel drinking vinegar-->
<!--          four dollar toast. Subway tile seitan shaman distillery tousled occupy marfa poutine kogi-->
<!--          organic artisan franzen solarpunk JOMO ascot. Listicle glossier everyday carry selfies DSA-->
<!--          letterpress. Asymmetrical tote bag gorpcore, schlitz tbh adaptogen venmo sriracha selvage-->
<!--          PBR&B slow-carb grailed.-->
<!--        </p>-->
<!--      </div>-->
      <Timeline :jobs="resume.jobs"/>
<!--      <Card :width="'full'" class="text-black">-->
<!--        <div class="min-w-0 flex-1">-->
<!--          <div class="mb-5">-->
<!--            <h2 class="text-2xl font-bold sm:truncate sm:text-3xl sm:tracking-tight mb-2">{{ resume.full_name }}</h2>-->
<!--            <h3 class="text-base/4 tracking-tight">{{ resume.address_line_one }} {{ resume.address_line_two }}</h3>-->
<!--            <h3 class="text-base/4 tracking-tight">{{ resume.city }}, {{ resume.state }} {{ resume.zip }}</h3>-->
<!--            <h3 class="text-base/4 tracking-tight">pdtnelson@gmail.com</h3>-->
<!--            <h3 class="text-base/4 tracking-tight">linkedin.com/in/pdtnelson</h3>-->
<!--          </div>-->

<!--          <div class="mb-5">-->
<!--            <h2 class="text-xl font-bold sm:truncate sm:text-2xl sm:tracking-tight mb-2">Skills</h2>-->
<!--            <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2">-->
<!--              <div v-for="(skill, index) in resume.skills" :key="index">-->
<!--                <p class="text-base">{{ skill }}</p>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="mb-5">-->
<!--            <h2 class="text-xl font-bold sm:truncate sm:text-2xl sm:tracking-tight mb-2">Experience</h2>-->
<!--            <div v-for="job in resume.jobs" :key="job.title" class="mb-2">-->
<!--              <JobDisplay :job="job" />-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="mb-5">-->
<!--            <div v-for="edu in resume.education" :key="edu.school" class="mb-2">-->
<!--              <EducationDisplay :education="edu" />-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="mb-5">-->
<!--            <div v-for="cert in resume.certifications" :key="cert.name" class="mb-2">-->
<!--              <CertificationDisplay :certification="cert" />-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="mb-5">-->
<!--            <h2 class="text-base font-bold sm:text-xl sm:tracking-tight mb-1">References</h2>-->
<!--            <h3 class="text-base/4 tracking-tight">Available Upon Request</h3>-->
<!--          </div>-->
<!--        </div>-->
<!--      </Card>-->
    </div>
  </main>
</template>

<style lang="scss">
</style>
