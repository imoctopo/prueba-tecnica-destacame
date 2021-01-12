<template>
  <div class="container">
    <Breadcrumb/>
    <h1 v-if="bus.id === null">New Bus</h1>
    <h1 v-else>Bus Editor</h1>
    <form @submit.prevent="saveBus()">
      <div class="form-group">
        <label for="driver">Driver</label>
        <select class="form-select" id="driver" v-model="driver_id">
          <option disabled>Select an element</option>
          <option
              v-for="driver in drivers"
              :value="driver.id"
              :key="driver.id"
              :selected="driver.id === driver_id"
          >
            {{ driver.name }} {{ driver.last_name }}
          </option>
        </select>
        <small v-for="(error, index) in errors.driver" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="licence-plate">Licence Plate</label>
        <input type="text" class="form-control" id="licence-plate" v-model="bus.licence_plate" required maxlength="6" minlength="6"/>
        <small v-for="(error, index) in errors.licence_plate" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Buses'}"
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
  name: "BusEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      bus: {
        id: null,
        driver: {
          id: null,
          name: null,
          last_name: null
        },
        licence_plate: null
      },
      driver_id: null,
      drivers: [],
      errors: {
        driver: [],
        licence_plate: []
      }
    };
  },
  mounted() {
    APIService.init();
    this.fetchDrivers();
    const id = this.$route.params.id;
    if (id !== "new")
      this.fetchBus(id);
  },
  methods: {
    async fetchDrivers() {
      const {data} = await APIService.list('drivers?all=1');
      this.drivers = data;
    },
    async fetchBus(id) {
      const {data} = await APIService.get('buses', id);
      this.bus = data;
      this.driver_id = data.driver ? data.driver.id : null;
    },
    async saveBus() {
      const driver = this.drivers.find(driver => driver.id === this.driver_id);
      let res = null;
      if (this.bus.id)
        res = await APIService.put(`buses`, this.bus.id, {...this.bus, driver: driver});
      else
        res = await APIService.post(`buses`, {...this.bus, driver: driver});
      console.log(res);
      if (res.error === null)
        await this.$router.push({name: "Buses"});
      else
        this.errors = res.error.data;
    }
  }
}
</script>

<style scoped></style>