<template>
  <div class="container">
    <Breadcrumb/>
    <h1 v-if="passenger.id === null">New Passenger</h1>
    <h1 v-else>Passenger Editor</h1>
    <form @submit.prevent="savePassenger()">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" v-model="passenger.name" required/>
        <small v-for="(error, index) in errors.name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="last-name">Last Name</label>
        <input type="text" class="form-control" id="last-name" v-model="passenger.last_name" required/>
        <small v-for="(error, index) in errors.last_name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Passengers'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
        </div>
        <div class="col d-flex flex-row-reverse">
          <button class="btn btn-success mt-4"><i class="bi bi-check"></i> Save</button>
        </div>
      </div>
    </form>
    <h2 class="mt-5">Tickets</h2>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th>Ride</th>
        <th>Seat</th>
        <th>Bus</th>
        <th>Driver</th>
        <th>Date</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="tickets.length === 0">
        <td colspan="4">No tickets found</td>
      </tr>
      <tr
          v-for="ticket in tickets"
          :key="ticket.id"
      >
        <td>{{ ticket.id }}</td>
        <td>
          <i class="bi bi-map"></i>
          Service: <strong>{{ ticket.ride.route.number }}</strong>
          Route: <strong>{{ ticket.ride.route.starting_address }} - {{ ticket.ride.route.ending_address }}</strong>
        </td>
        <td>{{ ticket.seat }}</td>
        <td>
          Licence plate: <strong>{{ ticket.ride.bus.licence_plate }}</strong>
        </td>
        <td>
          <span v-if="ticket.ride.bus.driver">
            driven by <strong>{{ ticket.ride.bus.driver.name }} {{ ticket.ride.bus.driver.last_name }}</strong>
          </span>
          <span v-else>No driver set yet...</span>
        </td>
        <td>{{ ticket.ride.schedule | moment("MMMM Do YYYY [at] h:mm A") }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Vue from "vue"
import Breadcrumb from "@/components/Breadcrumb";
import APIService from "@/common/api.service";

Vue.use(require('vue-moment'))

export default {
  name: "PassengerEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      passenger: {
        id: null,
        name: null,
        last_name: null
      },
      tickets: [],
      errors: {
        name: [],
        last_name: []
      }
    };
  },
  mounted() {
    APIService.init();
    const id = this.$route.params.id;
    if (id !== "new") {
      this.fetchPassenger(id);
      this.fetchTickets(id);
    }
  },
  methods: {
    async fetchPassenger(id) {
      const {data} = await APIService.get('passengers', id);
      this.passenger = data;
    },
    async fetchTickets(id) {
      const {data} = await APIService.list(`passengers/${id}/tickets`)
      this.tickets = data;
    },
    async savePassenger() {
      let res = null;
      if (this.passenger.id)
        res = await APIService.put(`passengers`, this.passenger.id, this.passenger);
      else
        res = await APIService.post(`passengers`, this.passenger);
      console.log(res);
      if (res.error === null)
        await this.$router.push({name: "Passengers"});
      else
        this.errors = res.error.data;
    }
  }
}
</script>

<style scoped></style>