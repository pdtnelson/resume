<script setup lang="ts">

import {
  createVNode,
  defineAsyncComponent, inject,
  onMounted,
  ref,
  render,
  useTemplateRef
} from 'vue'
import type { CreateResumeRequest, Job, Resume } from '@/domain/types.ts'
import JobInput from '@/components/JobInput.vue'
import { PlusIcon } from '@heroicons/vue/20/solid'
import JobDisplay from '@/components/JobDisplay.vue'
import { required } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core'
import type HttpClient from '@/http/http-client.ts'
import PillDisplayCombobox from '@/components/PillDisplayCombobox.vue'

const http: HttpClient = inject('http')!

const form = ref<CreateResumeRequest>({
  full_name: '',
  address_line_one: '',
  address_line_two: '',
  city: '',
  state: '',
  zip: null,
  skills: [],
  jobs: []
})
const rules = {
  full_name: { required },
  address_line_one: { required },
  city: { required },
  state: { required },
  zip: { required }
}
const v$ = useVuelidate(rules, form)
const skills = ref([])

const createResume = async () => {
  if (!(await v$.value.$validate())) return
  try {
    await http.client.post('/resumes', JSON.stringify(form.value))
  } catch (e) {
    console.error(`Error creating resume: ${e}`)
  }
}

const showJobInput = ref(false)
const addJob = (job: Job) => {
  form.value.jobs.push(job)
  showJobInput.value = false
}

</script>

<template>
  <form class="w-full" @submit="createResume()">
    <div class="flex justify-between">
      <div>
        <h2 class="text-base/7 font-semibold text-gray-900">Resume</h2>
        <p class="mt-1 text-sm/6 text-gray-600">Enter the details of your resume to be displayed on the public resume view.</p>
      </div>
      <div>
        <button type="button" :disabled="form.jobs.length < 1" :class="{'bg-indigo-500 cursor-not-allowed' : form.jobs.length < 1}" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="createResume">
          <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
          Save Resume
        </button>
      </div>
    </div>

    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
      <div class="mt-2 col-span-2">
        <label for="full-name" class="block text-sm/6 font-medium text-gray-900">Full Name</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="full-name" id="full-name" v-model="form.full_name" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-2">
        <label for="address-line-one" class="block text-sm/6 font-medium text-gray-900">Address Line One</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="address-line-one" id="address-line-one" v-model="form.address_line_one" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-2">
        <label for="address-line-two" class="block text-sm/6 font-medium text-gray-900">Address Line Two</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="address-line-two" id="address-line-two" v-model="form.address_line_two" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-2">
        <label for="city" class="block text-sm/6 font-medium text-gray-900">City</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="city" id="city" v-model="form.city" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-2">
        <label for="state" class="block text-sm/6 font-medium text-gray-900">State</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="state" id="state" v-model="form.state" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-2">
        <label for="zip" class="block text-sm/6 font-medium text-gray-900">Zip Code</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="number" name="zip" id="zip" v-model="form.zip" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
    </div>

    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
      <div class="col-span-4">
        <PillDisplayCombobox option-label="skills" :options="skills" v-model="form.skills" />
      </div>
    </div>

    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
      <div class="col-span-6">
        <div v-if="form.jobs.length <= 0 && !showJobInput" class="text-center">
          <svg class="mx-auto size-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path vector-effect="non-scaling-stroke" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
          </svg>
          <h3 class="mt-2 text-sm font-semibold text-gray-900">You added any jobs yet</h3>
          <p class="mt-1 text-sm text-gray-500">Get started by adding some jobs.</p>
          <div class="mt-6">
            <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="showJobInput = true">
              <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
              Add Job
            </button>
          </div>
        </div>
        <div v-if="showJobInput">
          <h2 class="text-2xl text-black">Jobs</h2>
          <JobInput @created="addJob" />
        </div>
        <div v-if="form.jobs && form.jobs.length > 0" v-for="job in form.jobs" :key="job.title">
          <JobDisplay :job="job" />
        </div>
        <div class="mt-6" v-if="form.jobs && form.jobs.length > 0">
          <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="showJobInput = true">
            <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
            Add Another Job
          </button>
        </div>
      </div>
    </div>

  </form>
</template>

<style scoped>

</style>
