<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import MainNav from "@/components/MainNav.vue";
import { computed } from 'vue'
import Foot from "@/components/Foot.vue";

const route = useRoute()
const showNav = computed(() => {
  return !route.path.includes('/admin')
})
</script>

<template>
<!--  <MainNav v-if="showNav"/>-->
  <RouterView />
  <Foot />
</template>

<style scoped>

</style>
