import '@/http/http-client'
import type { App } from 'vue'
import HttpClient from '@/http/http-client'

export default {
  install: (app: App, options = {}) => {
    app.provide('http', HttpClient.instance)
  }
}
