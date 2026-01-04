<script setup lang="ts">
import HttpClient from '@/http/http-client.ts'
import { inject, ref, onBeforeMount } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import type { BlogPost } from '@/domain/types.ts'
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import { PencilIcon } from '@heroicons/vue/20/solid'
import Editor from '@tinymce/tinymce-vue'

const http = inject<HttpClient>('http')!
const router = useRouter()
const route = useRoute()

const postId = route.params.id as string
const loading = ref(true)
const post = ref<BlogPost>({
  id: '',
  title: '',
  description: '',
  content: '',
  published_date: null
})

const rules = {
  title: { required },
  description: { required },
  content: { required }
}
const v$ = useVuelidate(rules, post)

const fetchPost = async () => {
  try {
    loading.value = true
    const response = await http.client.get<BlogPost>(`/posts/${postId}`)
    post.value = response.data
  
  } catch (e) {
    console.error('Failed to fetch blog post:', e)
    // Redirect back to blog management if post not found
    await router.push({ name: 'blog-management' })
  } finally {
    loading.value = false
  }
}

const updatePost = async () => {
  if (!(await v$.value.$validate())) return
  try {
    await http.client.put('/posts', JSON.stringify(post.value))
    await router.push({ name: 'blog-management'})
  } catch (e) {
    console.error('Failed to update post:', e)
  }
}

onBeforeMount(() => {
  fetchPost()
})
</script>

<template>
  <div v-if="loading" class="flex justify-center items-center h-64">
    <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
  </div>

  <form v-else class="w-full">
    <div class="flex justify-between">
      <div>
        <h2 class="text-base/7 font-semibold text-gray-900">Edit Blog Post</h2>
        <p class="mt-1 text-sm/6 text-gray-600">Update your blog post content.</p>
      </div>
      <div>
        <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="updatePost()">
          <PencilIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
          Update Post
        </button>
      </div>
    </div>

    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
      <div class="mt-2 col-span-2">
        <label for="title" class="block text-sm/6 font-medium text-gray-900">Title</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="title" id="title" v-model="post.title" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
        <p class="mt-2 text-sm text-red-600" v-if="v$.title.$error">
          Title is required.
        </p>
      </div>
      <div class="mt-2 col-span-4">
        <label for="description" class="block text-sm/6 font-medium text-gray-900">Description</label>
        <div class="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
          <input type="text" name="description" id="description" v-model="post.description" class="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-gray-900 placeholder:text-gray-400 focus:outline focus:outline-0 sm:text-sm/6" />
        </div>
        <p class="mt-2 text-sm text-red-600" v-if="v$.description.$error">
          Description is required.
        </p>
      </div>
    </div>

    <div class="mt-2">
      <label for="duties" class="block text-sm/6 font-medium text-gray-900">Post</label>
      <!-- TODO: Move key to env var-->
      <Editor
        v-model="post.content"
        api-key="ck3y717p8pc3y3eef6xukasfjj7mbd13z1dyv4xecq558526"
        :init="{
        plugins: 'lists link image table code help wordcount',
        toolbar: 'undo redo | blocks | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | help'
      }"
      />
      <p class="mt-2 text-sm text-red-600" v-if="v$.content.$error">
        Post content is required.
      </p>
    </div>
  </form>
</template>

<style scoped>

</style>