export type Job ={
  title: string
  start_date: Date
  end_date: Date | null
  duties: string[]
}

export type Resume = {
  id: string | null
  full_name: string
  address_line_one: string
  address_line_two: string
  city: string
  state: string
  zip: number
  jobs: Job[]
}

export type Profile = {
  id: string | null
  name: string
  job_title: string
  location: string
  salary: number
  profile_img_url: string
  text: string
}

export type ListResponse<T> = {
  data: T[]
  total: number
}
