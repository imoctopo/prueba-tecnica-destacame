<template>
  <div class="container">
    <Breadcrumb/>
    <h1 v-if="route.id === null">New Route</h1>
    <h1 v-else>Route Editor</h1>
    <form @submit.prevent="saveRoute()">
      <div class="form-group">
        <label for="number">Number</label>
        <input type="text" class="form-control" id="number" v-model="route.number" required/>
        <small v-for="(error, index) in errors.number" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="starting-address">Starting Address</label>
        <input type="text" class="form-control" id="starting-address" v-model="route.starting_address" required/>
        <small v-for="(error, index) in errors.starting_address" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="ending-address">Starting Address</label>
        <input type="text" class="form-control" id="ending-address" v-model="route.ending_address" required/>
        <small v-for="(error, index) in errors.ending_address" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Routes'}"
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
  name: "RouteEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      route: {
        id: null,
        number: null,
        starting_address: null,
        ending_address: null
      },
      errors: {
        number: [],
        starting_address: [],
        ending_address: []
      }
    };
  },
  mounted() {
    APIService.init();
    const id = this.$route.params.id;
    if (id !== "new")
      this.fetchRoute(id);
  },
  methods: {
    async fetchRoute(id) {
      const {data} = await APIService.get('routes', id);
      this.route = data;
    },
    async saveRoute() {
      let res = null;
      if (this.route.id)
        res = await APIService.put(`routes`, this.route.id, this.route);
      else
        res = await APIService.post(`routes`, this.route);
      if (res.error === null)
        await this.$router.push({name: "Routes"});
      else
        this.errors = res.error.data;
    }
  }
}
</script>

<style scoped>

</style>