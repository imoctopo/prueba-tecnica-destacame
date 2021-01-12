<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'Home' }">Destácame Rides</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link :to="{name:'Home'}" class="nav-link" active-class="active" exact>
              Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name:'Routes'}" class="nav-link" active-class="active" exact>
              Routes
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name:'Drivers'}" class="nav-link" active-class="active" exact>
              Drivers
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name:'Buses'}" class="nav-link" active-class="active" exact>
              Buses
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name:'Passengers'}" class="nav-link" active-class="active" exact>
              Passengers
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped></style>