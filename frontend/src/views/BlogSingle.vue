<script setup lang="ts">
import { useRoute } from 'vue-router'
import type { BlogPost } from '@/domain/types.ts'
import { inject, onBeforeMount, onMounted, ref } from "vue";
import type HttpClient from '@/http/http-client.ts'
import PageHeader from '@/components/PageHeader.vue'

const http = inject<HttpClient>('http')!
const route = useRoute()

const { id } = route.params
const post = ref<BlogPost>()

const fetchData = async () => {
  try {
    const response = await http.client.get<BlogPost>(`/posts/${id}`)
    post.value = response.data
  } catch (e) {
    console.log(e)
  }
}

onBeforeMount(() => {
  fetchData()
})

</script>
<template>
  <PageHeader v-if="post" :title="post.title" :desc="post.description" />
  <main class="container mx-auto mb-auto px-4 sm:px-6 lg:px-8 py-12">
    <article class="bg-white p-8 rounded-2xl shadow-lg max-w-4xl mx-auto leading-relaxed">
      <div v-if="post" class="article-content" v-html="post.content"></div>

      <div class="text-center">
        <RouterLink :to="{ name: 'blog' }" class="back-button inline-block mt-8 py-3 px-8 bg-emerald-500 text-white rounded-xl font-bold cursor-pointer shadow-md">
          &larr; Back to All Posts
        </RouterLink>
      </div>
    </article>
  </main>
</template>

<style lang="scss" scoped>
.article-content {
  h3 {
    font-size: 1.75rem; /* text-2xl */
    font-weight: 700; /* font-bold */
    color: #1a202c; /* Gray-900 */
    margin-top: 2rem;
    margin-bottom: 1rem;
  }

  p {
    margin-bottom: 1.25rem;
    font-size: 1.125rem;
    color: #475569; /* Slate-600 */
  }

  .article-content ul, .article-content ol {
    margin-left: 1.5rem;
    margin-bottom: 1.25rem;
    list-style-type: disc; /* Default for ul */
    color: #475569;

    li {
      margin-bottom: 0.5rem;
    }
  }

  .back-button {

  }
}
</style>
