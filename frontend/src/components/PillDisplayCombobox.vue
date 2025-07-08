<script setup lang="ts">
import { ref, toRef, computed } from 'vue'
import {
  Combobox,
  ComboboxInput,
  ComboboxOptions,
  ComboboxOption,
  TransitionRoot
} from '@headlessui/vue'
import { CheckIcon } from '@heroicons/vue/20/solid'
import Badge from '@/components/Badge.vue'

const props = defineProps<{
  title?: string
  options: string[]
  selectedOptions?: string[]
  optionLabel: string
}>()

const options = toRef(props, 'options')
const optionLabel = toRef(props, 'optionLabel')
const model = defineModel({ type: Array<string>, required: true })

const selected = ref<string>('')
const selectedOptions = toRef<string[]>(props.selectedOptions || [])
const query = ref('')

const filteredOptions = computed(() =>
  query.value === ''
    ? options.value
    : options.value.filter((option: string) =>
      option
        .toLowerCase()
        .replace(/\s+/g, '')
        .includes(query.value.toLowerCase().replace(/\s+/g, ''))
    )
)
const customOption = computed(() => {
  return query.value === '' ? null : query
})

function handleInput(option: string) {
  option.trim()
  if (option.length > 0) {
    if (!selectedOptions.value.includes(option)) {
      selectedOptions.value.push(option)
    }
    model.value = selectedOptions.value
  }
  // Remove options that have already been selected if they were present in the list
  if (options.value.includes(option)) {
    options.value.splice(options.value.indexOf(option), 1)
  }
}

function removeSelectedOption(option: string) {
  selectedOptions.value.splice(selectedOptions.value.indexOf(option), 1)
  options.value.push(option) // Put the option back so it can be reselected if accidentally removed
}
</script>

<template>
  <div>
    <Combobox v-model="selected">
      <div class="relative mt-1">
        <div
          class="block w-full cursor-default border-0 overflow-hidden rounded-md bg-white text-left shadow-sm focus:outline-none focus-visible:ring-2 focus-visible:ring-gray/75 focus-visible:ring-offset-2 focus-visible:ring-offset-teal-300 ring-1 ring-gray-300 ring-inset sm:text-sm"
        >
          <ComboboxInput
            class="w-full rounded-md border-0 bg-white py-1.5 pl-3 pr-12 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6"
            :placeholder="`Search or create ${optionLabel}...`"
            :display-value="() => (query ? `Search or create ${optionLabel}...` : query)"
            @change="query = $event.target.value"
            @keyup.enter="handleInput(selected)"
            @blur="query = ''"
          />
        </div>
        <TransitionRoot
          leave="transition ease-in duration-100"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
          @after-leave="query = ''"
        >
          <ComboboxOptions
            class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm"
          >
            <ComboboxOption
              v-for="option in filteredOptions"
              as="template"
              :key="option"
              :value="option"
              v-slot="{ selected, active }"
              @click="handleInput(option)"
              @keyup.enter="handleInput(option)"
            >
              <li
                class="relative cursor-default select-none py-2 pl-10 pr-4"
                :class="{
                  'bg-teal-600 text-white': active,
                  'text-gray-900': !active
                }"
              >
                <span
                  class="block truncate"
                  :class="{ 'font-medium': selected, 'font-normal': !selected }"
                >
                  {{ option }}
                </span>
                <span
                  v-if="selected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3"
                  :class="{ 'text-white': active, 'text-teal-600': !active }"
                >
                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                </span>
              </li>
            </ComboboxOption>
            <ComboboxOption
              as="template"
              v-slot="{ selected, active }"
              v-if="customOption"
              :value="customOption"
              @click="handleInput(customOption.value)"
            >
              <li
                class="relative cursor-default select-none py-2 pl-10 pr-4"
                :class="{
                  'bg-teal-600 text-white': active,
                  'text-gray-900': !active
                }"
              >
                <span
                  class="block truncate"
                  :class="{ 'font-medium': selected, 'font-normal': !selected }"
                >
                  Create new {{ optionLabel }}: {{ customOption }}
                </span>
                <span
                  v-if="selected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3"
                  :class="{ 'text-white': active, 'text-teal-600': !active }"
                >
                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                </span>
              </li>
            </ComboboxOption>
          </ComboboxOptions>
        </TransitionRoot>
      </div>
    </Combobox>
    <div class="mt-2">
      <badge
        :edit="true"
        v-for="option in selectedOptions"
        :key="option"
        @remove="removeSelectedOption(option)"
      >{{ option }}</badge
      >
    </div>
  </div>
</template>

<style scoped></style>

