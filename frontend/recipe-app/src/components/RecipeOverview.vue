<script lang="ts">
import { onBeforeMount, ref } from 'vue'
import axios from 'axios'
import router from '../router'

export default {
  setup() {
    const jsonDataRecipes = ref()

    onBeforeMount(async () => {
      await axios.get("http://localhost:5000/api/recipe/all-id-name")
        .then((response) => { jsonDataRecipes.value = response.data })
        .catch((error) => { console.log(error) })
    })

    const goToRecipe = (id: string) => {
      router.push({ name: 'recipe', params: { id: id } })
    }

    

    return {
      goToRecipe, jsonDataRecipes
    }
  }
}
</script>

<template>
  <div class="recipe-wrapper">
    <div class="card-recipe" v-for="recipe in jsonDataRecipes">
      {{ recipe.name }}
      <button class="go-button" @click="goToRecipe(recipe.uid_recipe)">Go To Recipe</button>
      <div class="info">Author: {{ recipe.author }}</div>
      <div class="info">Difficulty: {{ recipe.difficulty }}</div>
      <div class="info">Preperation time: {{ recipe.time_min }}</div>
    </div>
  </div>
</template>

<style scoped>

.info {
  font-size: smaller;
}
.card-recipe {
  border: solid none;
  margin-left: 20px;
  margin-top: 20px;
  padding: 15px;
  font-weight: bolder;
  width: 25rem;
  color: rgb(195, 198, 237);
  background-color: rgb(36, 49, 91);
  box-shadow: 2px 2px 5px rgb(3, 3, 3);
}

.card-recipe:hover {
  background-color: rgb(34, 51, 107);
}

.go-button {
  margin-top: 5px;
  padding: 10px;
  font-weight: bold;
  background-color: rgb(131, 38, 244);
  border: none;
  color: rgb(195, 198, 237);
  justify-self: right;
  float: right;
}

.go-button:hover{
  color: rgb(161, 165, 219);
  cursor: pointer;
}

button:active {
  background-color: rgb(72, 6, 153);
}

.recipe-wrapper {
  display: flex;
}
</style>