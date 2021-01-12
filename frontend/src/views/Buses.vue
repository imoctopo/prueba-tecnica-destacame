<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Buses</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'BusEditor', params: {id:'new'}}"
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
        <th>Driver</th>
        <th>Licence Plate</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="buses.length === 0">
        <td colspan="4">No buses found</td>
      </tr>
      <tr
          v-for="(bus, index) in buses"
          :key="index"
      >
        <td>{{ bus.id }}</td>
        <td class="col-6">
          <span v-if="bus.driver">{{ bus.driver.name }} {{ bus.driver.last_name }}</span>
          <span v-else>No driver set...</span>
        </td>
        <td class="col-6">{{ bus.licence_plate }}</td>
        <td>
          <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <router-link
                class="btn btn-warning mr-3"
                :to="{name: 'BusEditor', params: {id: bus.id}}"
            >
              <i class="bi bi-pencil"></i>
            </router-link>
            <button
                class="btn btn-danger"
                @click="deleteBus(bus.id)"
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
  name: "Buses",
  components: {
    Breadcrumb,
    Pagination
  },
  data() {
    return {
      buses: [],
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  methods: {
    async fetchBuses() {
      const {data} = await APIService.list(`buses?page=${this.activePage}`);
      this.buses = data.results;
      this.next = data.next;
      this.previous = data.previous;
      this.totalPages = data.total_pages;
    },
    async deleteBus(id) {
      await APIService.delete('buses', id);
      this.activePage = 1;
      await this.fetchBuses();
    }
  },
  watch: {
    activePage(page) {
      this.activePage = page;
      this.fetchBuses();
    }
  },
  mounted() {
    APIService.init();
    this.fetchBuses();
  }
}
</script>

<style scoped></style>