<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute()

const menu: {name: string, to: string}[] = [
  {
    name: 'Resume',
    to: 'resume'
  },
  {
    name: 'Contact Me',
    to: 'contact'
  }
]
</script>

<template>
  <header class="relative z-50 flex h-16 px-7 text-[#2c3e50] dark:text-neutral-300" :class="{ 'text-neutral-300': route.name === 'home' }">
    <div class="hidden sm:flex mx-auto w-full items-center justify-between pt-4 lg:py-2">
      <h1 class="text-2xl">Peter D. Nelson</h1>
      <div>
        <ul class="flex flex-row gap-2">
          <li v-for="item in menu" :key="item.name">
            <RouterLink class="text-[#2c3e50] dark:text-neutral-300 dark:hover:text-gray-500" :to="item.to" :class="{ 'text-neutral-300 hover:text-neutral-500': route.name === 'home' }">{{ item.name}}
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<style scoped>

</style>
