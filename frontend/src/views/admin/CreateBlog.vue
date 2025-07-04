<script setup lang="ts">
import HttpClient from '@/http/http-client.ts'
import { inject, ref } from 'vue'
import { useRouter } from 'vue-router'
import type { CreateBlogPostRequest } from '@/domain/types.ts'
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import { PlusIcon } from '@heroicons/vue/20/solid'
import Editor from '@tinymce/tinymce-vue'

const http = inject<HttpClient>('http')!
const router = useRouter()

const form = ref<CreateBlogPostRequest>({
  title: '',
  description: '',
  content: ''
})
const rules = {
  title: { required },
  description: { required },
  content: { required }
}
const v$ = useVuelidate(rules, form)

const createPost = async () => {
  if (!(await v$.value.$validate())) return
  try {
    await http.client.post('/posts', JSON.stringify(form.value))
    await router.push({ name: 'blog-management'})
  } catch (e) {
    console.error(e)
  }
}
</script>

<template>
  <form class="w-full">
    <div class="flex justify-between">
      <div>
        <h2 class="text-base/7 font-semibold text-gray-900">Resume</h2>
        <p class="mt-1 text-sm/6 text-gray-600">Author a new blog post.</p>
      </div>
      <div>
        <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="createPost()">
          <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
          Save Post
        </button>
      </div>
    </div>

    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
      <div class="mt-2 col-span-2">
        <label for="title" class="block text-sm/6 font-medium text-gray-900">Title</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="title" id="title" v-model="form.title" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
      <div class="mt-2 col-span-4">
        <label for="description" class="block text-sm/6 font-medium text-gray-900">Description</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="description" id="description" v-model="form.description" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
      </div>
    </div>

    <div class="mt-2">
      <label for="duties" class="block text-sm/6 font-medium text-gray-900">Post</label>
      <!-- TODO: Move key to env var-->
      <Editor
        v-model="form.content"
        api-key="ck3y717p8pc3y3eef6xukasfjj7mbd13z1dyv4xecq558526"
        :init="{
        plugins: 'lists link image table code help wordcount',
        toolbar: 'undo redo | blocks | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | help'
      }"
      />
    </div>
  </form>
</template>

<style scoped>

</style>
