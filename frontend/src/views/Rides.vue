<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Rides</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'RideEditor', params: {id:'new'}}"
          >
            <i class="bi bi-plus-circle"></i> New
          </router-link>
        </div>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th class="col-4">Route</th>
        <th class="col-4">Bus</th>
        <th class="col-4">Date</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="rides.length === 0">
        <td colspan="5">No rides found</td>
      </tr>
      <tr
          v-for="(ride, index) in rides"
          :key="index"
      >
        <td>{{ ride.id }}</td>
        <td>
          {{ ride.route.number }} [{{ ride.route.starting_address }} - {{ ride.route.ending_address }}]
        </td>
        <td>
          {{ ride.bus.licence_plate }}
          <span v-if="ride.bus.driver">driven by {{ ride.bus.driver.name }} {{ ride.bus.driver.last_name }}</span>
          <span v-else>no driver set yet...</span>
        </td>
        <td>{{ ride.schedule | moment("MMMM Do YYYY [at] h:mm A") }}</td>
        <td>
          <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <router-link
                class="btn btn-warning mr-3"
                :to="{name: 'RideEditor', params: {id: ride.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                class="btn btn-danger"
                @click="deleteRide(ride.id)"
            >
              <i class="bi bi-trash"></i>
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
    <Pagination :previous="previous" :next="next" :totalPages="totalPages" :activePage.sync="activePage"/>
  </div>
</template>

<script>
import Vue from "vue"
import APIService from "@/common/api.service";
import Breadcrumb from "@/components/Breadcrumb";
import Pagination from "@/components/Pagination";

Vue.use(require("vue-moment"))

export default {
  name: "Rides",
  components: {
    Breadcrumb,
    Pagination
  },
  data() {
    return {
      rides: [],
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  methods: {
    async fetchRides() {
      const {data} = await APIService.list(`rides?page=${this.activePage}`);
      this.rides = data.results;
      this.next = data.next;
      this.previous = data.previous;
      this.totalPages = data.total_pages;
    },
    async deleteRide(id) {
      await APIService.delete('rides', id);
      this.activePage = 1;
      await this.fetchRides();
    }
  },
  watch: {
    activePage(page) {
      this.activePage = page;
      this.fetchRides();
    }
  },
  mounted() {
    APIService.init();
    this.fetchRides();
  }
}
</script>

<style scoped>

</style>