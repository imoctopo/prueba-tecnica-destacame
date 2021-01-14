<template>
  <nav>
    <ol class="breadcrumb" v-if="!new_breadcrumb">
      <li class="breadcrumb-item"
          v-for="(bread, index) in breadcrumb"
          :key="index"
          :class="{'active': breadcrumb.length - 1 === index, 'cursor-pointer': breadcrumb.length - 1 !== index}"
          @click="routeTo(index)"
      >
        {{ bread.name }}
      </li>
    </ol>
    <ol class="breadcrumb" v-else>
      <li class="breadcrumb-item"
          v-for="(bread, index) in new_breadcrumb"
          :key="index"
          :class="{'active': new_breadcrumb.length - 1 === index, 'cursor-pointer': new_breadcrumb.length - 1 !== index}"
          @click="routeTo(index)"
      >
        {{ bread.name }}
      </li>
    </ol>
  </nav>
</template>

<script>
export default {
  name: "Breadcrumb",
  props: {
    new_breadcrumb: {
      type: Array,
    }
  },
  data() {
    return {
      breadcrumb: []
    }
  },
  watch: {
    '$route'() {
      this.update();
    }
  },
  mounted() {
    this.update();
  },
  methods: {
    routeTo(target) {
      if (this.breadcrumb[target].link)
        this.$router.push(this.breadcrumb[target].link)
    },
    update() {
      this.breadcrumb = this.$route.meta.breadcrumb;
    }
  }
}
</script>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}

.breadcrumb {
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: .75rem 1rem;
  margin-bottom: 1rem;
  list-style: none;
  background-color: #e9ecef;
  border-radius: .25rem;
}
</style>