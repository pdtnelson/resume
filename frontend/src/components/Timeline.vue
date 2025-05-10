<script setup lang="ts">
import type { Job } from "@/domain/types.ts";

const { jobs } = defineProps<{ jobs: Job[]}>()
</script>

<template>
  <div class="timeline relative flex flex-1 flex-col min-h-full dark:before:bg-white before:absolute before:flex before:flex-1 before:top-0 before:min-h-full before:w-[4px] before:left-1/2 before:-ml-0.5">
    <div class="timeline-element relative my-16 after:clear-both after:table" v-for="(job, index) in jobs">
      <span class="timeline-element-icon h-14 w-14 absolute top-0 left-1/2 -ml-7">
        <!-- GitHub logo as placeholder. TODO: Remove/Replace -->
        <img :src="job.company_logo_url" alt="">
      </span>
      <div
        class="timeline-element-content relative bg-white w-[44%] ml-0 p-6 rounded-[.25rem] text-black shadow-md"
        :class="{'float-right': index % 2 != 0 }"
      >
        <div class="mb-2">
          <h1 class="text-2xl font-semibold">{{ job.title }}</h1>
          <h2 class="text-xl">{{ job.company }}</h2>
          <h3 class="text-lg">{{ job.start_date?.toLocaleString() }} - {{ job.end_date? job.end_date.toLocaleString() : 'Present'}}</h3>
        </div>
        <p>Same shaman banjo, you probably haven't heard of them fingerstache salvia waistcoat.
          Poutine glossier gochujang air plant gluten-free, put a bird on it biodiesel VHS aesthetic dreamcatcher activated charcoal.
          Beard sriracha ascot, williamsburg paleo mlkshk taxidermy.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.timeline::before {
  background-image: linear-gradient(180deg,rgba(255, 255, 255, 1) 0%, rgba(24, 24, 24, 1) 2%, rgba(24, 24, 24, 1) 91%, rgba(255, 255, 255, 1) 100%);
}
@media(prefers-color-scheme: dark) {
  .timeline::before {
    background-image: linear-gradient(180deg,rgba(24, 24, 24, 1) 0%, rgba(255, 255, 255, 1) 2%, rgba(255, 255, 255, 1) 91%, rgba(24, 24, 24, 1) 100%);
  }
}
</style>
