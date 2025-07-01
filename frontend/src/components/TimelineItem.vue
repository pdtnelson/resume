<script setup lang="ts">
import type { Job } from "@/domain/types.ts";
import { ref } from "vue";
import type { DateTime } from "luxon";

const { job } = defineProps<{job: Job}>()
const show = ref<Boolean>(false)

const formatDateRange = (startDate: DateTime, endDate: DateTime | null) => {
  const endDateString = endDate ? `${endDate.monthLong} ${endDate.year}` : 'Present'
  return `${startDate.monthLong} ${startDate.year} - ${endDateString}`
}
</script>

<template>
  <div class="timeline-item">
    <div class="timeline-card w-full md:w-5/12">
      <h3 class="text-2xl font-bold text-gray-900 mb-1">{{ job.title }}</h3>
      <p class="text-lg font-semibold text-blue-700 mb-2">{{ job.company }}<span class="text-gray-500 text-base font-normal"> | {{ formatDateRange(job.start_date!, job.end_date) }}</span></p>
      <p class="text-gray-700 text-base leading-relaxed">
        {{ job.description }}
      </p>
      <button class="toggle-button" @click="show = !show">
        Show Responsibilities
        <svg class="w-4 h-4 ml-2 transition-transform duration-300 transform" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
      </button>
      <Transition>
        <div class="job-responsibilities" v-show="show">
          <ul class="text-gray-600">
            <li v-for="duty in job.duties">{{ duty }}</li>
          </ul>
        </div>
      </Transition>
    </div>
  </div>
</template>

<style scoped>
.timeline-card {
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 0.75rem; /* rounded-lg */
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  flex-grow: 1; /* Allow card to take available width */
  transition: transform 0.3s ease-in-out;
  cursor: pointer; /* Indicate clickability for toggle */
  border-left: 4px solid #3b82f6; /* Left border accent */
}
.timeline-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 25px -5px rgba(0, 0, 0, 0.2);
}
.timeline-item {
  position: relative;
  margin-bottom: 2rem;
  display: flex;
  justify-content: flex-end; /* Default to right side */
  padding-right: 3rem; /* Space for the circle */
  align-items: center; /* Vertically align items */
}
.timeline-item:nth-child(even) .timeline-card {
  border-right: 4px solid #3b82f6; /* Right border accent for alternate side */
  border-left: none;
}
.toggle-button {
  background-color: #64748b; /* Gray-600 */
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
  margin-top: 1rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.toggle-button:hover {
  background-color: #475569; /* Gray-700 */
}
.toggle-button svg {
  margin-left: 0.5rem;
}

.job-responsibilities {
  overflow: hidden;
  transition: max-height 0.5s ease-out; /* Smooth transition */
  padding-top: 0.5rem; /* Space above list when expanded */
}
.job-responsibilities.expanded {
  max-height: 500px; /* Adjust as needed, sufficiently large to show content */
}
.job-responsibilities ul {
  list-style-type: disc;
  margin-left: 1.5rem;
  padding-left: 0.5rem;
}
.job-responsibilities li {
  margin-bottom: 0.25rem;
}
/* Responsive adjustments for timeline on small screens */
@media (max-width: 768px) {
  .timeline-item {
    justify-content: flex-start; /* All items on the right side on mobile */
    padding-left: 3rem; /* Consistent padding */
    padding-right: 0;
  }
  .timeline-item::before {
    left: calc(1rem - 8px);
    right: auto;
  }
  .timeline-card {
    width: 100%;
  }
}
/* transition states */
.v-enter-active, .v-leave-active {
  transition: max-height 0.7s ease-in-out;
  overflow: hidden;
}

.v-enter-from, .v-leave-to {
  max-height: 0;
}

.v-enter-to, .v-leave-from {
  max-height: 500px;
}
</style>
