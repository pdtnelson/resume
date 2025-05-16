import axios from 'axios'
import axiosRetry from 'axios-retry'
import type { AxiosInstance } from 'axios'
import { DateTime } from 'luxon'
import { cloneDeep } from 'lodash'
import { useNotificationStore } from "@/stores/notification.ts";



export default class HttpClient {
  toast = useNotificationStore()
  static #instance: HttpClient
  client: AxiosInstance

  private constructor() {
    this.client = axios.create({
      baseURL: `${import.meta.env.VITE_BASE_API_URL}`,
      headers: {
        'Content-Type': 'application/json'
      }
    })
    axiosRetry(this.client, { retries: 5, retryDelay: axiosRetry.exponentialDelay })
    const token = localStorage?.user && JSON.parse(localStorage?.user)?.token
    if (token) {
      this.client.defaults.headers.common['Authorization'] = `Bearer ${token}`
    }

    this.client.interceptors.response.use(
      (response) => {
        const dateFields = [
          'created_at',
          'updated_at',
          'start_date',
          'end_date'
        ]

        const maybeCoerceDatestringToLuxon = (
          datestr?: string
        ): DateTime<true> | string | undefined => {
          if (datestr) {
            const dtMaybe = DateTime.fromISO(datestr)
            if (dtMaybe.isValid) {
              return dtMaybe
            }
          }
          return datestr
        }

        const coerceLuxonDeep = (unk: any): any => {
          if (Array.isArray(unk)) {
            return unk.map((nested: unknown) => coerceLuxonDeep(nested))
          } else if (unk !== null && typeof unk === 'object') {
            Object.keys(unk).forEach((key) => {
              if (typeof unk[key] === 'object') {
                unk[key] = coerceLuxonDeep(unk[key])
              } else if (
                typeof unk[key] === 'string' &&
                dateFields.includes(key) &&
                unk[key].trim().length > 0
              ) {
                unk[key] = maybeCoerceDatestringToLuxon(unk[key])
              }
            })
          }
          return unk
        }

        return {
          ...response,
          data: coerceLuxonDeep(response.data ? cloneDeep(response.data) : response.data)
        }
      },
      (e) => {
        console.error('Error:', e)
        return Promise.reject(e)
      }
    )
  }

  public static get instance(): HttpClient {
    if (!HttpClient.#instance) {
      HttpClient.#instance = new HttpClient()
    }
    return HttpClient.#instance
  }

  public setAuthHeader(token: string) {
    this.client.defaults.headers.common['Authorization'] = `Bearer ${token}`
  }

  public clearAuthHeader() {
    delete this.client.defaults.headers.common['Authorization']
  }

  public handleError(error: any, showToast: boolean = false, message: string = '') {
    if (showToast) {
      this.toast.show('error', message ? message : error.message)
    }
    console.error(error.message)
  }
}
