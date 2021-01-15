<template>
  <div class="container">
    <Breadcrumb :new_breadcrumb="breadcrumb"/>
    <h1 v-if="ticket.id === null && ride.id">New Ticket for Ride #{{ ride.id }} [{{ ride.route.starting_address }} - {{ ride.route.ending_address }}]</h1>
    <h1 v-else>Ticket Editor for Ride <span v-if="ride.id">#{{ ride.id }} [{{ ride.route.starting_address }} - {{ ride.route.ending_address }}]</span></h1>
    <form @submit.prevent="savePassenger()">
      <div class="form-group">
        <label for="passenger">Passenger</label>
        <select class="form-control" id="passenger" v-model="passengerId" required>
          <option disabled>Select an element</option>
          <option
              v-for="passenger in passengers"
              :value="passenger.id"
              :key="passenger.id"
              :selected="passenger.id === passengerId"
          >
            {{ passenger.name }} {{ passenger.last_name }}
          </option>
        </select>
        <small v-for="(error, index) in errors.passenger" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="seat">Seat</label>
        <select class="form-control" id="seat" v-model="seat" required>
          <option disabled v-if="seats.length > 0">Select an element</option>
          <option disabled v-else>Sold Out!</option>
          <option
              v-for="seat_ in seats"
              :value="seat_"
              :key="seat_"
              :selected="seat_ === ticket.seat"
          >
            {{ seat_ }}
          </option>
        </select>
        <small v-for="(error, index) in errors.seat" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Rides'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
          &nbsp;
          <router-link
              class="btn btn-primary mt-4"
              :to="`/rides/${ride.id}`"
          >
            <i class="bi bi-arrow-left"></i> Back To The Ride
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
  name: "TicketEditor",
  components: {
    Breadcrumb
  },
  data() {
    return {
      breadcrumb: null,
      ticket: {
        id: null,
        ride: null,
        passenger: null,
        seat: null
      },
      rideId: null,
      ride: {
        id: null
      },
      passengers: null,
      passengerId: null,
      seat: null,
      seats: [],
      errors: {
        passenger: [],
        seat: []
      }
    }
  },
  mounted() {
    APIService.init();
    this.rideId = this.$route.params.rideId;
    this.fetchRide();
    this.fetchPassengers();
    this.fetchFreeSeats();
    const id = this.$route.params.id;
    if (id !== 'new') this.fetchTicket(id);
    else this.createBreadcrumbs('new');
  },
  methods: {
    async fetchTicket(id) {
      const {data} = await APIService.get(`rides/${this.rideId}/tickets`, id);
      this.ticket = data;
      this.passengerId = data.passenger.id;
      this.seat = data.seat;
      this.orderSeats(this.seat);
      if (id)
        this.createBreadcrumbs(this.ticket.id);
    },
    async fetchRide() {
      const {data} = await APIService.get('rides', this.rideId);
      this.ride = data;
    },
    async fetchPassengers() {
      const {data} = await APIService.list('passengers?all=1')
      this.passengers = data;
    },
    async fetchFreeSeats() {
      const {data} = await APIService.list(`rides/${this.rideId}/free-seats`);
      this.seats = data;
      if (this.ticket.id) {
        this.orderSeats(this.ticket.seat);
      }
    },
    async savePassenger() {
      let res = null;
      if (this.ticket.id)
        res = await APIService.put(`rides/${this.rideId}/tickets`, this.ticket.id, {passenger: this.passengerId, seat: this.seat});
      else
        res = await APIService.post(`rides/${this.rideId}/tickets`, {passenger: this.passengerId, seat: this.seat});
      if (res.error === null)
        await this.$router.push(`/rides/${this.rideId}`);
      else
        this.errors = res.error.data;
    },
    orderSeats(ticketSeat) {
      this.seats.push(ticketSeat);
      this.seats.sort((a, b) => a - b);
    },
    createBreadcrumbs(id) {
      let [home, rides, ride, ticketEditor] = this.$route.meta.breadcrumb;
      ride.name = this.rideId;
      ride.link = `/rides/${this.rideId}`;
      ticketEditor.name = id === 'new' ? 'New Ticket' : 'Ticket #' + id
      this.breadcrumb = [home, rides, ride, ticketEditor];
    }
  }
}
</script>

<style scoped>

</style>