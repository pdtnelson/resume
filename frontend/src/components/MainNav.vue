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
  <header class="flex items-center justify-between h-16 px-7 dark:text-white">
    <h1 class="text-2xl">Peter D. Nelson</h1>
    <div>
      <ul class="flex flex-row gap-2">
        <li v-for="item in menu" :key="item.name"><RouterLink class="text-gray-800 dark:text-white dark:hover:text-gray-500" :to="item.to">{{ item.name}}</RouterLink></li>
      </ul>
    </div>
  </header>
</template>

<style scoped>

</style>
