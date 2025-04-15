import { DateTime } from 'luxon'


export type Job ={
  title: string
  company: string
  start_date: DateTime
  end_date: DateTime | null
  description: string
}

export type Resume = {
  id: string
  full_name: string
  address_line_one: string
  address_line_two: string
  city: string
  state: string
  zip: number | null
  skills: string[]
  jobs: Job[]
}

export type CreateResumeRequest = Omit<Resume, 'id'>

export type Profile = {
  id: string | null
  name: string
  job_title: string
  location: string
  salary: number
  profile_img_url: string
  text: string
}

export type PagedResponse<T> = {
  data: T[]
  total: number
}
