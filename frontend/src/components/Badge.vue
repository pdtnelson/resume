<script setup lang="ts">
import { cn } from '@/lib/utils'

const props = defineProps<{ edit?: boolean; variant?: string; class?: string }>()
let classDefaults =
  'inline-flex items-center gap-x-0.5 rounded-md px-2 py-1 text-xs font-medium ring-1 ring-inset mb-2'
if (props.variant === 'info') {
  classDefaults += ' bg-white ring-black text-black'
} else {
  classDefaults += ' text-blue-700 bg-blue-50 ring-blue-700/10'
}
</script>
<template>
  <span :class="cn(classDefaults, props.class)">
    <slot />
    <button
      type="button"
      class="group relative -mr-1 h-3.5 w-3.5 rounded-sm hover:bg-blue-600/20"
      @click="$emit('remove')"
      v-if="edit"
    >
      <span class="sr-only">Remove</span>
      <svg
        viewBox="0 0 14 14"
        class="h-3.5 w-3.5 stroke-blue-700/50 group-hover:stroke-blue-700/75"
      >
        <path d="M4 4l6 6m0-6l-6 6" />
      </svg>
      <span class="absolute -inset-1" />
    </button>
  </span>
</template>

<style scoped></style>
