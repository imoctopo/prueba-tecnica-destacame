<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Passengers</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'PassengerEditor', params: {id:'new'}}"
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
        <th>Name</th>
        <th>Last Name</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="passengers.length === 0">
        <td colspan="4">No passengers found</td>
      </tr>
      <tr
          v-for="(passenger, index) in passengers"
          :key="index"
      >
        <td>{{ passenger.id }}</td>
        <td class="col-6">{{ passenger.name }}</td>
        <td class="col-6">{{ passenger.last_name }}</td>
        <td>
          <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <router-link
                title="Edit"
                class="btn btn-warning mr-3"
                :to="{name: 'PassengerEditor', params: {id: passenger.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deletePassenger(passenger.id)"
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
import Breadcrumb from "@/components/Breadcrumb";
import Pagination from "@/components/Pagination";
import APIService from "@/common/api.service";

export default {
  name: "Passengers",
  components: {
    Breadcrumb,
    Pagination
  },
  data() {
    return {
      passengers: [],
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  methods: {
    async fetchPassengers() {
      const {data} = await APIService.list(`passengers?page=${this.activePage}`);
      this.passengers = data.results;
      this.next = data.next;
      this.previous = data.previous;
      this.totalPages = data.total_pages;
    },
    async deletePassenger(id) {
      await APIService.delete('passengers', id);
      this.activePage = 1;
      await this.fetchPassengers();
    }
  },
  watch: {
    activePage(page) {
      this.activePage = page;
      this.fetchPassengers();
    }
  },
  mounted() {
    APIService.init();
    this.fetchPassengers();
  }
}
</script>

<style scoped></style>