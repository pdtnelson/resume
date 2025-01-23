import axios from 'axios'
import axiosRetry from 'axios-retry'
import type { AxiosInstance } from 'axios'



export default class HttpClient {
  static #instance: HttpClient
  client: AxiosInstance

  private constructor() {
    this.client = axios.create({
      baseURL: `${location.protocol}//${location.host}/api/`,
      headers: {
        'Content-Type': 'application/json'
      }
    })
    axiosRetry(this.client, { retries: 5, retryDelay: axiosRetry.exponentialDelay })
    const token = localStorage?.user && JSON.parse(localStorage?.user)?.token
    if (token) {
      this.client.defaults.headers.common['Authorization'] = `Bearer ${token}`
    }
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
}
