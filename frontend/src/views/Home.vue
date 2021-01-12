<template>
  <div class="container">
    <h1>Home</h1>
    <Breadcrumb/>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>

import Breadcrumb from "@/components/Breadcrumb";

export default {
  name: 'Home',
  components: {
    Breadcrumb
  }
}
</script>
