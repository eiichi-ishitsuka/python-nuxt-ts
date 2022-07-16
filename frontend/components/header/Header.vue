<template>
    <v-app-bar color="primary" id="app-bar">
        <template v-slot:prepend>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Photos</v-app-bar-title>

        <v-menu open-on-hover>
            <template v-slot:activator="{ props }">
                <v-btn v-bind="props" icon="mdi-dots-vertical">
                </v-btn>
            </template>
            <v-list dark dense>
                <v-list-item v-for="menu in items" :key="menu.no" link>
                    <v-list-item-title>{{ menu.title }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </v-app-bar>
</template>

<script>
export default {
    data: () => ({
        items: [
            { no: 1, title: 'About us' },
            { no: 2, title: 'プライバシーポリシー' },
            { no: 3, title: '利用規約' },
            { no: 4, title: 'ログアウト' },
        ],
        closeOnContentClick: true,
    }),
}
</script>