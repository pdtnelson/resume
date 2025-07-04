import { createRouter, createWebHistory } from 'vue-router'
import type { RouteLocationNormalizedGeneric } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import Resume from '@/views/Resume.vue'
import Contact from '@/views/Contact.vue'
import AdminDashboard from '@/views/admin/AdminDashboard.vue'
import AdminProfile from '@/views/admin/AdminProfile.vue'
import AdminResume from '@/views/admin/AdminResume.vue'
import CreateResume from '@/views/admin/CreateResume.vue'
import Blog from '@/views/Blog.vue'
import { jwtDecode } from 'jwt-decode'
import type { UserJWTPayload } from '@/domain/types.ts'
import SignIn from '@/views/SignIn.vue'
import BlogSingle from '@/views/BlogSingle.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'PDT Nelson',
        requiresAuth: false
      }
    },
    {
      path: '/resume',
      name: 'resume',
      component: Resume,
      meta: {
        title: 'PDT Resume',
        requiresAuth: false
      }
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact,
      meta: {
        title: 'Contact Me',
        requiresAuth: false
      }
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog,
      meta: {
        title: 'Blog',
        requiresAuth: false
      }
    },
    {
      path: '/blog/:id',
      name: 'blog-single',
      component: BlogSingle,
      meta: {
        title: 'Blog',
        requiresAuth: false
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn,
      meta: {
        title: 'Sign In',
        requiresAuth: false
      }
    },
    {
      path: '/admin',
      name: 'admin-dashboard',
      component: AdminDashboard,
      meta: {
        title: 'Admin Dashboard',
        requiresAuth: true
      },
      children: [
        {
          path: 'profile',
          name: 'admin-profile',
          component: AdminProfile
        },
        {
          path: 'resume',
          name: 'admin-resume',
          component: AdminResume
        },
        {
          path: 'resume/create',
          name: 'resume-create',
          component: CreateResume
        }
      ]
    }
  ],
})

router.beforeEach(async (to, from) => {
  window.document.title = to.meta.title
  const validAuth = await checkAuth(to)
  if (to.meta.requiresAuth && !validAuth) {
    return { name: 'signin' }
  }
})
async function checkAuth(to: RouteLocationNormalizedGeneric) {
  return to.matched.some((record) => {
    const token = localStorage.getItem('token')
    if (!token) {
      return false
    }
    const decoded = jwtDecode<UserJWTPayload>(token)
    return !(record.meta.requiresRole && decoded.roles.includes('SITE_ADMIN'))
  })
}

export default router

export {}

declare module 'vue-router' {
  interface RouteMeta {
    title: string
    requiresAuth?: boolean
  }
}
