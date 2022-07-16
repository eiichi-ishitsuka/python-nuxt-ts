<template>
    <v-app>
        <div>
            <header>
                <Header />
            </header>
            <v-main>
                <slot />
            </v-main>
        </div>
    </v-app>
</template>

<script setup>
import Header from "@/components/header/Header.vue";
</script>