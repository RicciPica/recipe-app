<script lang="ts">
import { onBeforeMount, ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

export default {
    setup() {
        const jsonDataRecipeInfo = ref()
        const jsonDataRecipeStep = ref()
        const router:any = useRoute()
        const strImageDateURL = ref<string>("")
        var prefixImage = new String("data:image/png;base64,")
        const strURLRecipe: string = "http://localhost:5000/api/recipe/".concat(router.params.id)
        const strURLRecipeSteps: string = "http://localhost:5000/api/recipe/steps/".concat(router.params.id)

        onBeforeMount(async () => {
            await axios.get(strURLRecipe)
                .then((response) => { jsonDataRecipeInfo.value = response.data })
                .catch((error) => { console.log(error) })

            await axios.get(strURLRecipeSteps)
                .then((response) => { jsonDataRecipeStep.value = response.data })
                .catch((error) => { console.log(error) })
                
            var image = new Image()
            image.src = prefixImage.concat(jsonDataRecipeInfo.value.image_file_name)
            strImageDateURL.value = image.src

        })

        return {
            jsonDataRecipeInfo, strImageDateURL, jsonDataRecipeStep
        }
    }
}
</script>

<template>
    <div class="info-container" v-if="jsonDataRecipeInfo">
        <img v-bind:src="strImageDateURL" width="auto" height="300">
        <div>
            <div class="recipe-name">{{ jsonDataRecipeInfo.name }}</div>
            <div class="recipe-info">{{ jsonDataRecipeInfo.difficulty }}</div>
            <div class="recipe-info">{{ jsonDataRecipeInfo.time_min }}</div>
        </div>
    </div>
    <div class="description" v-for="step in jsonDataRecipeStep">
        <div>{{ step.step_description }}</div>
    </div>
</template>

<style scoped>
.info-container {
    display: flex;
    padding: 1rem;
}

.info-container div {
    padding-left: 0.5rem;
}

.recipe-name {
    font-weight: bolder;
    font-size: x-large;
}

.recipe-info {
    font-size: large;
}

.description {
    padding-left: 1rem;
    padding-top: 1rem;
}

.description div {
    border: solid;
}
</style>