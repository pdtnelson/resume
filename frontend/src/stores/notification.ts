import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useNotificationStore = defineStore('notification', () => {
  const visible = ref(false)
  const variant = ref('')
  const message = ref('')

  function show(type: string, text: string) {
    variant.value = type
    message.value = text
    visible.value = true
    setTimeout(() => {
      visible.value = false
    }, 3000)
  }

  return {
    visible,
    message,
    variant,
    show
  }
})
