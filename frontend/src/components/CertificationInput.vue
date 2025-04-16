<script setup lang="ts">
import type { Certification } from '@/domain/types.ts'
import { ref } from 'vue'
import { required } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core'

const emit = defineEmits<{'created': [certification: Certification]}>()

const certification = ref<Certification>({
  name: '',
  issuer: '',
  certification_url: ''
})
const rules = {
  name: { required },
  issuer: { required }
}

const v$ = useVuelidate(rules, certification)
const validateAndEmit = async () => {
  if (!(await v$.value.$validate())) return
  emit('created', certification.value)
}
</script>

<template>
  <div class="mt-2">
    <label for="name" class="block text-sm/6 font-medium text-gray-900">Name</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="certification.name" type="text" name="name" id="name" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="issuer" class="block text-sm/6 font-medium text-gray-900">Issuer</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="certification.issuer" type="text" name="issuer" id="issuer" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="certification_url" class="block text-sm/6 font-medium text-gray-900">Certification Url</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="certification.certification_url" type="text" name="certification_url" id="certification_url" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <button @click.prevent="validateAndEmit()" class="mt-2 inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save Certification</button>
</template>

<style scoped>

</style>
