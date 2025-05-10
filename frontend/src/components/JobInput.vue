<script setup lang="ts">
import useVuelidate from '@vuelidate/core'
import Editor from '@tinymce/tinymce-vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

import type { Job } from '@/domain/types.ts'
import { ref } from 'vue'
import { required } from '@vuelidate/validators'

const emit = defineEmits<{
  created: [job: Job]
}>()

const job = ref<Job>({
  title: '',
  company: '',
  company_logo_url: '',
  start_date: null,
  end_date: null,
  description: ''
})
const rules = {
  title: { required },
  start_date: { required },
  description: { required }
}
const v$ = useVuelidate(rules, job)
const validateAndEmit = async () => {
  if (!(await v$.value.$validate())) return
  emit('created', job.value)
}
</script>

<template>
  <div class="mt-2">
    <label for="title" class="block text-sm/6 font-medium text-gray-900">Job Title</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="job.title" type="text" name="title" id="title" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="company" class="block text-sm/6 font-medium text-gray-900">Company</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="job.company" type="text" name="company" id="company" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="company-logo-url" class="block text-sm/6 font-medium text-gray-900">Company Logo Url</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="job.company_logo_url" type="text" name="company-logo-url" id="company-logo-url" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2 grid gap-2 grid-cols-2">
    <div>
      <label for="title" class="block text-sm/6 font-medium text-gray-900">Start Date</label>
      <VueDatePicker v-model="job.start_date" />
    </div>
    <!-- TODO: add option to specify you currently work at this job -->
    <div>
      <label for="title" class="block text-sm/6 font-medium text-gray-900">End Date</label>
      <VueDatePicker v-model="job.end_date" />
    </div>
  </div>
  <div class="mt-2">
    <label for="duties" class="block text-sm/6 font-medium text-gray-900">Job Description</label>
    <!-- TODO: Move key to env var-->
    <Editor
      v-model="job.description"
      api-key="ck3y717p8pc3y3eef6xukasfjj7mbd13z1dyv4xecq558526"
      :init="{
        plugins: 'lists link image table code help wordcount',
        toolbar: 'undo redo | blocks | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | help'
      }"
    />
  </div>
  <button @click.prevent="validateAndEmit()" class="mt-2 inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save Job</button>
</template>

<style scoped>

</style>
