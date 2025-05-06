<script setup lang="ts">
import type { Education } from '@/domain/types.ts'
import { ref } from 'vue'
import { required } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core'

const emit = defineEmits<{created: [education: Education]}>()

const education = ref<Education>({
  school: '',
  city: '',
  state: '',
  description: ''
})
const rules = {
  school: { required },
  city: { required },
  state: { required },
  description: { required }
}

const v$ = useVuelidate(rules, education)
const validateAndEmit = async () => {
  if (!(await v$.value.$validate())) return
  emit('created', education.value)
}
</script>

<template>
  <div class="mt-2">
    <label for="school" class="block text-sm/6 font-medium text-gray-900">School</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="education.school" type="text" name="school" id="school" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="city" class="block text-sm/6 font-medium text-gray-900">City</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="education.city" type="text" name="city" id="city" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="state" class="block text-sm/6 font-medium text-gray-900">State</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="education.state" type="text" name="state" id="state" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <div class="mt-2">
    <label for="description" class="block text-sm/6 font-medium text-gray-900">Description</label>
    <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
      <input v-model="education.description" type="text" name="description" id="description" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
    </div>
  </div>
  <button @click.prevent="validateAndEmit()" class="mt-2 inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save Education</button>
</template>

<style scoped>

</style>
