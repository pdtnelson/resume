<script setup lang="ts">
const { title, desc } = defineProps<{ title: string; desc: string }>()
</script>

<template>
  <header class="hero-background flex min-h-[20vh] sm:min-h-12 items-center justify-center text-white px-4 sm:px-6 lg:px-8">
    <div class="container mx-auto text-center py-8">
      <h1
        class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-2 drop-shadow-md"
      >
        {{ title }}
      </h1>
      <p class="text-lg sm:text-xl font-light opacity-90 max-w-3xl mx-auto">
        {{ desc }}
      </p>
    </div>
  </header>
</template>

<style scoped>
header {
  background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
}
</style>
