<template>
  <div class="container">
    <Breadcrumb/>
    <div class="row">
      <div class="col">
        <h1>Drivers</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'DriverEditor', params: {id:'new'}}"
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
        <th width="50%">Name</th>
        <th width="50%">Last Name</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="drivers.length === 0">
        <td colspan="4">No drivers found</td>
      </tr>
      <tr
          v-for="(driver, index) in drivers"
          :key="index"
      >
        <td>{{ driver.id }}</td>
        <td>{{ driver.name }}</td>
        <td>{{ driver.last_name }}</td>
        <td>
          <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'DriverEditor', params: {id: driver.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteDriver(driver.id)"
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
  name: 'Drivers',
  components: {
    Breadcrumb,
    Pagination
  },
  data() {
    return {
      drivers: [],
      activePage: 1,
      totalPages: 1,
      next: null,
      previous: null
    }
  },
  methods: {
    async fetchDrivers() {
      const {data} = await APIService.list(`drivers?page=${this.activePage}`);
      this.drivers = data.results;
      this.next = data.next;
      this.previous = data.previous;
      this.totalPages = data.total_pages;
    },
    async deleteDriver(id) {
      await APIService.delete('drivers', id);
      this.activePage = 1;
      await this.fetchDrivers();
    }
  },
  watch: {
    activePage(page) {
      this.activePage = page;
      this.fetchDrivers();
    }
  },
  mounted() {
    APIService.init();
    this.fetchDrivers();
  }
}
</script>