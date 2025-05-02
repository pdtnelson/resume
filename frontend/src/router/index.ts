import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Resume from "@/views/Resume.vue";
import Contact from "@/views/Contact.vue";
import AdminDashboard from '@/views/admin/AdminDashboard.vue'
import AdminProfile from '@/views/admin/AdminProfile.vue'
import AdminResume from '@/views/admin/AdminResume.vue'
import CreateResume from '@/views/admin/CreateResume.vue'
import Blog from '@/views/Blog.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/resume',
      name: 'resume',
      component: Resume
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog
    },
    {
      path: '/admin',
      name: 'admin-dashboard',
      component: AdminDashboard,
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
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
