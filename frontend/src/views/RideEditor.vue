<template>
  <div class="container">
    <Breadcrumb/>
    <h1 v-if="ride.id === null">New Ride</h1>
    <h1 v-else>Ride Editor</h1>
    <form @submit.prevent="saveRide()">
      <div class="form-group">
        <label for="route">Route</label>
        <select class="form-control" id="route" v-model="route_id" required>
          <option disabled>Select an element</option>
          <option
              v-for="route in routes"
              :value="route.id"
              :key="route.id"
              :selected="route.id === route_id"
          >
            {{ route.number }} [{{ route.starting_address }} - {{ route.ending_address }}]
          </option>
        </select>
        <small v-for="(error, index) in errors.route" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="bus">Bus</label>
        <select class="form-control" id="bus" v-model="bus_id" required>
          <option disabled>Select an element</option>
          <option
              v-for="bus in buses"
              :value="bus.id"
              :key="bus.id"
              :selected="bus.id === bus_id"
          >
            {{ bus.licence_plate }}
            <span v-if="bus.driver">driven by {{ bus.driver.name }} {{ bus.driver.last_name }}</span>
            <span v-else>no driver set yet...</span>
          </option>
        </select>
        <small v-for="(error, index) in errors.bus" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="schedule">Schedule</label>
        <input type="datetime-local" class="form-control" id="schedule" v-model="ride.schedule" required maxlength="6" minlength="6"/>
        <small v-for="(error, index) in errors.schedule" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Rides'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
        </div>
        <div class="col d-flex flex-row-reverse">
          <button class="btn btn-success mt-4"><i class="bi bi-check"></i> Save</button>
        </div>
      </div>
    </form>
    <div v-if="ride.id">
      <div class="row mt-5">
        <div class="col">
          <h2>Tickets</h2>
        </div>
        <div class="col">
          <div class="d-flex flex-row-reverse">
            <router-link
                class="btn btn-success float-right"
                :to="{name: 'TicketEditor', params: {rideId: ride.id, id: 'new'}}"
            >
              <i class="bi bi-plus-circle"></i> New
            </router-link>
          </div>
        </div>
      </div>
      <table class="table table-bordered mb-5">
        <thead>
        <tr>
          <th>#</th>
          <th width="23%">Passenger</th>
          <th width="5%">Seat</th>
          <th width="23%">Bus</th>
          <th width="23%">Driver</th>
          <th width="26%">Date</th>
          <th>Actions</th>
        </tr>
        </thead>
        <tbody>
        <tr v-if="tickets.length === 0">
          <td colspan="7">No tickets found</td>
        </tr>
        <tr
            v-for="ticket in tickets"
            :key="ticket.id"
        >
          <td>{{ ticket.id }}</td>
          <td>
            {{ ticket.passenger.name }} {{ ticket.passenger.last_name }}
          </td>
          <td align="center">{{ ticket.seat }}</td>
          <td>
            Licence plate: <strong>{{ ride.bus.licence_plate }}</strong>
          </td>
          <td>
            <span v-if="ride.bus.driver">
              {{ ride.bus.driver.name }} {{ ride.bus.driver.last_name }}
            </span>
            <span v-else>No driver set yet...</span>
          </td>
          <td>{{ ride.schedule | moment("MMMM Do YYYY [at] h:mm A") }}</td>
          <td>
            <div class="btn-group">
              <router-link
                  title="Edit"
                  class="btn btn-warning"
                  :to="{name: 'TicketEditor', params: {rideId: ride.id, id: ticket.id}}"
              >
                <i class="bi bi-eye"></i>
              </router-link>
              <button
                  title="Delete"
                  class="btn btn-danger"
                  @click="deleteTicket(ticket.id)"
              >
                <i class="bi bi-trash"></i>
              </button>
            </div>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Vue from "vue"
import Breadcrumb from "@/components/Breadcrumb";
import APIService from "@/common/api.service";

Vue.use(require('vue-moment'))

export default {
  name: "RideEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      ride: {
        id: null,
        route: null,
        bus: null,
        schedule: null
      },
      route_id: null,
      bus_id: null,
      buses: [],
      routes: [],
      tickets: [],
      errors: {
        route: [],
        bus: [],
        schedule: []
      }
    };
  },
  mounted() {
    APIService.init();
    this.fetchRoutes();
    this.fetchBuses();
    const id = this.$route.params.id;
    if (id !== "new") {
      this.fetchRide(id);
      this.fetchTickets(id);
    }
  },
  methods: {
    async fetchRoutes() {
      const {data} = await APIService.list('routes?all=1');
      this.routes = data;
    },
    async fetchBuses() {
      const {data} = await APIService.list('buses?all=1');
      this.buses = data;
    },
    async fetchRide(id) {
      const {data} = await APIService.get('rides', id);
      this.ride = data;
      this.bus_id = data.bus.id;
      this.route_id = data.route.id;
    },
    async fetchTickets(id) {
      const {data} = await APIService.list(`rides/${id}/tickets`)
      this.tickets = data;
    },
    async saveRide() {
      const route = this.routes.find(route => route.id === this.route_id);
      const bus = this.buses.find(bus => bus.id === this.bus_id);
      let res = null;
      if (this.ride.id)
        res = await APIService.put(`rides`, this.ride.id, {...this.ride, route: route.id, bus: bus.id});
      else
        res = await APIService.post(`rides`, {...this.ride, route: route.id, bus: bus.id});
      if (res.error === null)
        await this.$router.push({name: "Rides"});
      else
        this.errors = res.error.data;
    },
    async deleteTicket(id) {
      await APIService.delete(`rides/${this.ride.id}/tickets`, id);
      await this.fetchTickets(this.ride.id);
    }
  }
}
</script>

<style scoped></style>