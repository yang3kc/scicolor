<script setup>
import { ref } from "vue";

const hello = ref("Hello World");
</script>

<template>
    <h1>{{ hello }}</h1>
</template>