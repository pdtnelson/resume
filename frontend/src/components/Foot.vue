<script setup lang="ts">
import { DateTime } from 'luxon'
</script>

<template>
  <footer class="bg-gray-900 text-white text-center p-8 mt-12 rounded-t-2xl shadow-inner">
    <p class="text-sm mb-2">&copy; {{ DateTime.now().year }} PDTNelson. All rights reserved.</p>
    <div class="mt-4 flex justify-center space-x-6">
      <a
        href="https://linkedin.com/in/pdtnelson"
        target="_blank"
        class="text-blue-400 hover:text-blue-200 transition-colors text-lg"
        >LinkedIn</a
      >
    </div>
  </footer>
</template>

<style scoped></style>
