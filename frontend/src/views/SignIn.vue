<script setup lang="ts">
import { ref, inject, onBeforeMount } from 'vue'
import router from '@/router'
import type HttpClient from '@/http/http-client'
import { email, required } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core'
import { ExclamationCircleIcon } from '@heroicons/vue/20/solid'

type SignInForm = {
  email: string,
  password: string
}
const http: HttpClient = inject('http')!

const form = ref<SignInForm>({ email: '', password: '' })
const rules = {
  email: { required, email },
  password: { required }
}
const v$ = useVuelidate(rules, form)
const processing = ref(false)
async function login() {
  try {
    // PDT: Extra safety check: Don't submit invalid forms.
    processing.value = true
    if (!(await v$.value.$validate())) return
    const r = await http.client.post<{ token: string }>('/login', JSON.stringify(form.value))
    const token = r.data.token
    http.setAuthHeader(token)
    localStorage.setItem('token', token)
    processing.value = false
    await(router.push({ name: 'admin-dashboard' }))
  } catch (e) {
    http.handleError(e, true, 'Login failed. Please check your credentials and try again.')
    processing.value = false
  } finally {
    processing.value = false
  }
}
</script>

<template>
  <main class="flex items-center justify-center mb-auto">
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:mt-auto">

      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <form action="#" method="POST" @submit.prevent>
          <div class="h-24">
            <label for="email" class="block text-sm font-medium leading-6">Email address</label>
            <div class="relative mt-1 rounded-md shadow-sm">
              <input
                type="email"
                name="email"
                id="email"
                class="block text-black w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6"
                :class="{ 'text-red-900 ring-red-300': v$.email.$error }"
                placeholder="you@example.com"
                aria-invalid="true"
                aria-describedby="email-error"
                @blur="v$.email.$touch"
                v-model="form.email"
              />
              <div
                class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3"
                v-if="v$.email.$error"
              >
                <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              </div>
            </div>
            <p class="mt-2 text-sm text-red-600" v-if="v$.email.$error">
              Please enter a valid email address.
            </p>
          </div>

          <div class="h-24">
            <label for="email" class="block text-sm font-medium leading-6">Password</label>
            <div class="relative mt-1 rounded-md shadow-sm">
              <input
                type="password"
                name="password"
                id="password"
                class="block text-black w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6"
                :class="{ 'text-red-900 ring-red-300': v$.password.$error }"
                placeholder="Password"
                aria-invalid="true"
                aria-describedby="email-error"
                @blur="v$.password.$touch"
                v-model="form.password"
              />
              <div
                class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3"
                v-if="v$.password.$error"
              >
                <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              </div>
            </div>
            <p class="mt-2 text-sm text-red-600" v-if="v$.password.$error">Password is required.</p>
          </div>

          <div class="mt-2">
            <button @click="login" type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
