import { DateTime } from 'luxon'
import type { JwtPayload } from "jwt-decode";

// TODO: Add job logo field
export type Job = {
  title: string
  company: string
  description: string
  start_date: DateTime | null
  end_date: DateTime | null
  duties: string[]
}

export type Education = {
  school: string
  city: string
  state: string
  description: string
}

export type Certification = {
  name: string
  issuer: string
  certification_url?: string
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
  education: Education[]
  certifications: Certification[] | null
}

export type CreateResumeRequest = Omit<Resume, 'id'>

// TODO: Change string | null to use omitted create request
export type Profile = {
  id: string | null
  name: string
  job_title: string
  location: string
  salary: number
  profile_img_url: string
  text: string
  tracking_uuid: string
}

export type PagedResponse<T> = {
  data: T[]
  total: number
}

export interface UserJWTPayload extends JwtPayload {
  user_id: string
  email: string
  first_name: string
  last_name: string
  roles: string[]
}

export type BlogPost = {
  id: string,
  title: string,
  description: string,
  published_date: DateTime,
  content: string
}

export type CreateBlogPostRequest = Omit<BlogPost, 'id' | 'published_date'>
