<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Routes</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'RouteEditor', params: {id:'new'}}"
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
        <th>Number</th>
        <th class="col-4">Starting Address</th>
        <th class="col-4">Ending Address</th>
        <th class="col-4">Average Seats Sold</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="routes.length === 0">
        <td colspan="5">No routes found</td>
      </tr>
      <tr
          v-for="(route, index) in routes"
          :key="index"
      >
        <td>{{ route.id }}</td>
        <td>
          {{ route.number }}
        </td>
        <td>{{ route.starting_address }}</td>
        <td>{{ route.ending_address }}</td>
        <td>{{ route.passenger_average || 0 }} [ {{ route.total_tickets }} tickets in {{ route.total_rides }} rides ]</td>
        <td>
          <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <router-link
                title="Edit"
                class="btn btn-warning mr-3"
                :to="{name: 'RouteEditor', params: {id: route.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteRoute(route.id)"
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
import APIService from "@/common/api.service";
import Breadcrumb from "@/components/Breadcrumb";
import Pagination from "@/components/Pagination";

export default {
  name: "Routes",
  components: {
    Breadcrumb,
    Pagination
  },
  data() {
    return {
      routes: [],
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  methods: {
    async fetchRoutes() {
      const {data} = await APIService.list(`routes?page=${this.activePage}`);
      this.routes = data.results;
      this.next = data.next;
      this.previous = data.previous;
      this.totalPages = data.total_pages;
    },
    async deleteRoute(id) {
      await APIService.delete('routes', id);
      this.activePage = 1;
      await this.fetchRoutes();
    }
  },
  watch: {
    activePage(page) {
      this.activePage = page;
      this.fetchRoutes();
    }
  },
  mounted() {
    APIService.init();
    this.fetchRoutes();
  }
}
</script>

<style scoped></style>