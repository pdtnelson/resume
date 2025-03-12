<script setup lang="ts">
import { formatCurrency } from '@/lib/utils.ts'
import type HttpClient from '@/http/http-client.ts'
import { inject, onBeforeMount, ref } from 'vue'
import type { ListResponse, Profile } from '@/domain/types.ts'

const http: HttpClient = inject('http')!
const profiles = ref<Profile[]>()
const fetchData = async () => {
  try {
    const response = await http.client.get<ListResponse<Profile>>('/profiles')
    profiles.value = response.data.data
  } catch (e) {
    console.error(e)
  }
}
onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <div class="w-full">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-gray-900">Profiles</h1>
        <p class="mt-2 text-sm text-gray-700">A list of all the profiles you have created for different applications</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Add user</button>
      </div>
    </div>
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <table class="min-w-full divide-y divide-gray-300">
            <thead>
            <tr>
              <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Company Name</th>
              <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Job Title</th>
              <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Location</th>
              <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Salary</th>
              <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                <span class="sr-only">Edit</span>
              </th>
            </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
            <tr v-for="profile in profiles" :key="profile.name">
              <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">{{ profile.name }}</td>
              <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{ profile.jobTitle }}</td>
              <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{ profile.location }}</td>
              <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{ formatCurrency(profile.salary) }}</td>
              <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                <a href="#" class="text-indigo-600 hover:text-indigo-900"
                >Edit<span class="sr-only">, {{ profile.name }}</span></a
                >
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
