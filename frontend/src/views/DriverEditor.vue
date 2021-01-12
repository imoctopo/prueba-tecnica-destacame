<template>
  <div class="container">
    <Breadcrumb/>
    <h1 v-if="driver.id === null">New Driver</h1>
    <h1 v-else>Driver Editor</h1>
    <form @submit.prevent="saveDriver()">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" v-model="driver.name" required/>
        <small v-for="(error, index) in errors.name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="last-name">Last Name</label>
        <input type="text" class="form-control" id="last-name" v-model="driver.last_name" required/>
        <small v-for="(error, index) in errors.last_name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Drivers'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
        </div>
        <div class="col d-flex flex-row-reverse">
          <button class="btn btn-success mt-4"><i class="bi bi-check"></i> Save</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import Breadcrumb from "@/components/Breadcrumb";
import APIService from "@/common/api.service";

export default {
  name: "DriverEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      driver: {
        id: null,
        name: null,
        last_name: null
      },
      errors: {
        name: [],
        last_name: []
      }
    };
  },
  mounted() {
    APIService.init();
    const id = this.$route.params.id;
    if (id !== "new")
      this.fetchDriver(id);
  },
  methods: {
    async fetchDriver(id) {
      const {data} = await APIService.get('drivers', id);
      this.driver = data;
    },
    async saveDriver() {
      let res = null;
      if (this.driver.id)
        res = await APIService.put(`drivers`, this.driver.id, this.driver);
      else
        res = await APIService.post(`drivers`, this.driver);
      if (res.error === null)
        await this.$router.push({name: "Drivers"});
      else
        this.errors = res.error.data;
    }
  }
}
</script>

<style scoped></style>