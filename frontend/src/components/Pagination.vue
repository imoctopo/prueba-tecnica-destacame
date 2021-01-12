<template>
  <nav>
    <ul class="pagination">
      <li class="page-item" v-if="previous">
        <button class="page-link" @click="updateActivePage(previous)">Previous</button>
      </li>
      <li class="page-item"
          v-for="page in totalPages"
          :key="page"
          :class="{active: activePage === page}"
          @click="updateActivePage(page)"
      >
        <button class="page-link">{{ page }}</button>
      </li>
      <li class="page-item" v-if="next">
        <button class="page-link" @click="updateActivePage(next)">Next</button>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    next: {
      type: Number,
    },
    previous: {
      type: Number,
    },
    activePage: {
      type: Number,
      required: true
    },
    totalPages: {
      type: Number,
      required: true
    }
  },
  methods: {
    updateActivePage(page) {
      if (page === this.activePage) return;
      this.$emit("update:activePage", page);
    }
  }
}
</script>

<style scoped></style>