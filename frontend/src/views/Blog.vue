<script setup lang="ts">
import PageHeader from '@/components/PageHeader.vue'
import { inject, onBeforeMount, ref } from 'vue'
import HttpClient from '@/http/http-client.ts'
import type { BlogPost, PagedResponse } from '@/domain/types.ts'
import type { DateTime } from 'luxon'

const http = inject<HttpClient>('http')!

const title = 'Thoughts from the Software Trenches'
const desc = 'Disclaimer: The following content represents my personal thoughts and opinions on many things and is not recommended for human consumption.'
const posts = ref<BlogPost[]>([])

const fetchData = async () => {
  try {
    const response = await http.client.get<PagedResponse<BlogPost>>('/posts')
    posts.value = response.data.data
  } catch (e) {
    console.log(e)
  }
}

const formatDate = (date: DateTime): string => {
  return `${date.monthLong} ${date.day}, ${date.year}`
}
onBeforeMount(() => {
  fetchData()
})
</script>

<template>
  <PageHeader :title="title" :desc="desc" />
  <main class="container mx-auto mb-auto px-4 sm:px-6 lg:px-8 py-12">
    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div
        class="flex flex-col justify-between bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg min-h-64"
        v-for="post in posts"
      >
        <div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">{{ post.title }}</h3>
          <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-06-15"> {{ formatDate(post.published_date) }}</time></p>
          <p class="text-gray-700 mb-4 leading-relaxed">{{ post.description }}</p>
        </div>
        <RouterLink :to="{ name: 'blog-single', params: { id: post.id } }" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</RouterLink>
      </div>
    </section>
  </main>
</template>

<style scoped>
</style>
