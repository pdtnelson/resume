<script setup lang="ts">
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
  <header class="relative z-50 flex h-16 px-7 dark:text-white">
    <div class="hidden sm:flex mx-auto w-full items-center justify-between pt-4 lg:py-2">
      <h1 class="text-2xl">Peter D. Nelson</h1>
      <div>
        <ul class="flex flex-row gap-2">
          <li v-for="item in menu" :key="item.name"><RouterLink class="text-gray-800 dark:text-white dark:hover:text-gray-500" :to="item.to">{{ item.name}}</RouterLink></li>
        </ul>
      </div>
    </div>
  </header>
</template>

<style scoped>

</style>
