<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import MainNav from "@/components/MainNav.vue";
</script>

<template>
  <MainNav />
  <RouterView />
</template>

<style scoped>

</style>
