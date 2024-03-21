<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <div class="nav-start-icon">My Familiys Recipe Database</div>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/recipes">Recipes</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
  nav {
    display: flex;
    justify-content: left;
    background-color: rgb(36, 49, 91);
  }

  nav a {
    padding: 10px;
    font-size: x-large;
  }

  .nav-start-icon {
    text-decoration: none;
    color: rgb(0, 0, 0);
    font-size: x-large;
    padding: 10px;
    padding-right: 50px;
    padding-left: 25px;
    font-weight: bolder;
    background-color: rgb(112, 40, 235);
    border-bottom-right-radius: 30px;
    border-top-right-radius: 30px;
    text-align: center;
  }


</style>
