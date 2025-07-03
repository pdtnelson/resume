<script setup lang="ts">
import PageHeader from '@/components/PageHeader.vue'
import { inject, onMounted, ref } from "vue";
import HttpClient from '@/http/http-client.ts'
import type { BlogPost, PagedResponse } from "@/domain/types.ts";
import type { DateTime } from "luxon";

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
onMounted(() => {
  fetchData()
})
</script>

<template>
  <PageHeader :title="title" :desc="desc" />
  <main class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">

    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <!-- Blog Post Card 1 -->
      <div
        class="flex flex-col justify-between bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg"
        v-for="post in posts"
      >
        <div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">{{ post.title }}</h3>
          <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-06-15"> {{ formatDate(post.published_date) }}</time></p>
          <p class="text-gray-700 mb-4 leading-relaxed">{{ post.description }}</p>
        </div>
        <RouterLink :to="{ name: 'blog-single', params: { id: post.id } }" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</RouterLink>
      </div>

      <!-- Blog Post Card 2 -->
      <div class="flex flex-col justify-between bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg">
        <div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">Mastering Kubernetes Deployments</h3>
          <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-05-28">May 28, 2025</time></p>
          <p class="text-gray-700 mb-4 leading-relaxed">
            Tips and tricks for efficient and robust Kubernetes deployments,
            from basic YAML to advanced Helm charts and CI/CD pipelines...
          </p>
        </div>
        <a href="path/to/blog-post-1.html" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</a>
      </div>

      <!-- Blog Post Card 3 -->
      <div class="bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg">
        <h3 class="text-2xl font-bold text-gray-900 mb-2">Clean Code Practices for Python</h3>
        <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-05-10">May 10, 2025</time></p>
        <p class="text-gray-700 mb-4 leading-relaxed">
          Strategies for writing maintainable, readable, and testable Python code.
          Focus on SOLID principles and common design patterns...
        </p>
        <a href="path/to/blog-post-1.html" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</a>
      </div>

      <!-- Blog Post Card 4 -->
      <div class="bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg">
        <h3 class="text-2xl font-bold text-gray-900 mb-2">Effective Remote Team Collaboration</h3>
        <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-04-20">April 20, 2025</time></p>
        <p class="text-gray-700 mb-4 leading-relaxed">
          Lessons learned and best practices for fostering strong collaboration
          and productivity within distributed engineering teams...
        </p>
        <a href="path/to/blog-post-1.html" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</a>
      </div>

      <!-- Blog Post Card 5 -->
      <div class="bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg">
        <h3 class="text-2xl font-bold text-gray-900 mb-2">The Power of Asynchronous Programming in Go</h3>
        <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-03-05">March 05, 2025</time></p>
        <p class="text-gray-700 mb-4 leading-relaxed">
          Exploring goroutines and channels for building highly concurrent
          and performant applications in Go...
        </p>
        <a href="path/to/blog-post-1.html" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</a>
      </div>

      <!-- Blog Post Card 6 -->
      <div class="bg-white p-6 rounded-xl border-l-4 border-l-emerald-500 shadow-lg">
        <h3 class="text-2xl font-bold text-gray-900 mb-2">Building Resilient APIs with Rate Limiting</h3>
        <p class="text-sm text-gray-500 mb-4">Published on <time datetime="2025-02-18">February 18, 2025</time></p>
        <p class="text-gray-700 mb-4 leading-relaxed">
          Strategies and implementation patterns for protecting your API
          endpoints from abuse and ensuring fair usage with rate limiting...
        </p>
        <a href="path/to/blog-post-1.html" class="font-semibold text-blue-600 hover:text-blue-700 hover:text-decoration-line">Read More &rarr;</a>
      </div>

    </section>

  </main>
</template>

<style scoped>
.page-header {
  background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
  min-height: 20vh; /* Shorter header than homepage hero */
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
