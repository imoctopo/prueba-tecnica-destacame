<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Rides</h1>
      </div>
      <div class="col">
        <input class="form-control" type="number" placeholder="Filter by percentage of sold seats..." v-model="percentage" @keyup="fetchRides(percentage)">
      </div>
      <div class="col">
        <router-link
            class="btn btn-success float-right ml-2"
            :to="{name: 'RideEditor', params: {id:'new'}}"
        >
          <i class="bi bi-plus-circle"></i> New
        </router-link>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th width="24%">Route</th>
        <th width="28%">Bus</th>
        <th width="28%">Date</th>
        <th width="20%">Free Seats</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="rides.length === 0">
        <td colspan="6">No rides found</td>
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
        <td align="center">{{ ride.free_seats.length }} [{{ 100 - (ride.free_seats.length * 10) }}% tickets sold]</td>
        <td>
          <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'RideEditor', params: {id: ride.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <router-link
                title="New Ticket"
                class="btn btn-success"
                :to="{name: 'TicketEditor', params: {rideId: ride.id, id: 'new'}}"
            >
              <i class="bi bi-card-heading"></i>
            </router-link>
            <button
                title="Delete"
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
      percentage: null,
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  mounted() {
    APIService.init();
    this.fetchRides(0);
  },
  methods: {
    async fetchRides(percentage) {
      const {data} = await APIService.list(`rides?page=${this.activePage}&percentage=${percentage}`);
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
  }
}
</script>

<style scoped>

</style>