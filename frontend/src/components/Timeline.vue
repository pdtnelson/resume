<script setup lang="ts">
import type { Job } from "@/domain/types.ts";
import TimelineItem from "@/components/TimelineItem.vue";

const { jobs } = defineProps<{ jobs: Job[]}>()
</script>

<template>
  <section class="timeline">
    <!-- Job Experience 1 -->
    <TimelineItem />

    <!-- Job Experience 2 -->
    <TimelineItem />
    <!-- Job Experience 3 -->
    <TimelineItem />
  </section>
</template>

<style scoped>
/* Timeline specific styles */
.timeline {
  position: relative;
  padding: 2rem 0;
  max-width: 900px; /* Limit timeline width */
  margin: 0 auto; /* Center the timeline */
}
.timeline::before {
  content: '';
  position: absolute;
  left: 50%; /* Center the line */
  top: 0;
  width: 4px;
  height: 100%;
  background-color: #cbd5e1; /* Gray-300 for the line */
  transform: translateX(-50%);
  border-radius: 2px;
}
.timeline-item {
  position: relative;
  margin-bottom: 2rem;
  display: flex;
  justify-content: flex-end; /* Default to right side */
  padding-right: 3rem; /* Space for the circle */
  align-items: center; /* Vertically align items */
}
.timeline-item:nth-child(even) {
  justify-content: flex-start; /* Alternate to left side */
  padding-left: 3rem; /* Space for the circle */
  padding-right: 0;
}

/* Responsive adjustments for timeline on small screens */
@media (max-width: 768px) {
  .timeline::before {
    left: 1rem; /* Move line to the left edge */
    transform: translateX(0);
  }
  .timeline-item {
    justify-content: flex-start; /* All items on the right side on mobile */
    padding-left: 3rem; /* Consistent padding */
    padding-right: 0;
  }
  .timeline-item::before {
    left: calc(1rem - 8px); /* Align circle with the line */
    right: auto;
  }
  .timeline-card {
    width: 100%; /* Take full width on mobile */
  }
}

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
.timeline-item:nth-child(even) .timeline-card {
  border-right: 4px solid #3b82f6; /* Right border accent for alternate side */
  border-left: none;
}
.timeline-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 25px -5px rgba(0, 0, 0, 0.2);
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
  max-height: 0; /* Initially hidden */
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
</style>
