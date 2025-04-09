<script setup lang="ts">
import { cn } from '@/lib/utils'

const props = defineProps<{ width?: string; class?: string }>()
let classDefaults = 'flex flex-row p-4 sm:px-6 lg:px-8 rounded-lg shadow bg-white'
if (props.width) {
  classDefaults += ` w-${props.width}`
}
</script>

<template>
  <div class="flex flex-1 justify-center">
    <div :class="cn(classDefaults, props.class)">
      <slot />
    </div>
  </div>
</template>

<style scoped></style>
