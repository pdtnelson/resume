<script setup lang="ts">
import HttpClient from '@/http/http-client.ts'
import { inject, onBeforeMount, ref } from "vue";
import type { BlogPost, PagedResponse } from "@/domain/types.ts";
import { PlusIcon } from "@heroicons/vue/20/solid";
import { useRouter } from 'vue-router'

const http = inject<HttpClient>('http')!
const router = useRouter()

const posts = ref<BlogPost[]>([])

const fetchData = async () => {
  try {
    const response = await http.client.get<PagedResponse<BlogPost>>('/posts')
    posts.value = response.data.data
  } catch (e) {
    console.error(e)
  }
}

onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <div class="w-full" :class="posts.length > 0 ? '' : 'flex justify-center items-center'">
    <!-- Blog Posts List -->
    <div v-if="posts.length > 0" class="space-y-4">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-900">Blog Posts</h2>
        <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="router.push({name: 'blog-create'})">
          <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
          New Post
        </button>
      </div>
      
      <div class="bg-white shadow overflow-hidden sm:rounded-md">
        <ul role="list" class="divide-y divide-gray-200">
          <li v-for="post in posts" :key="post.id" class="px-6 py-4 hover:bg-gray-50 cursor-pointer" @click="router.push({ name: 'blog-edit', params: { id: post.id } })">
            <div class="flex items-center justify-between">
              <div class="flex-1">
                <h3 class="text-lg font-medium text-gray-900">{{ post.title }}</h3>
                <p v-if="post.description" class="mt-1 text-sm text-gray-600">{{ post.description }}</p>
              </div>
              <div class="text-sm text-gray-500">
                {{ post.published_date }}
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center">
      <svg class="mx-auto size-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path vector-effect="non-scaling-stroke" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
      </svg>
      <h3 class="mt-2 text-sm font-semibold text-gray-900">You haven't created any posts yet</h3>
      <p class="mt-1 text-sm text-gray-500">Get started by creating your first post.</p>
      <div class="mt-6">
        <button type="button" class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="router.push({name: 'blog-create'})">
          <PlusIcon class="-ml-0.5 mr-1.5 size-5" aria-hidden="true" />
          New Post
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
