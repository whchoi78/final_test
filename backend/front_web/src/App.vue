<template>
    <div>
        <header></header>
        <content></content>
        <footer></footer>
    </div>
</template>

<script>
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";

export default {
    data: function() {
        return {
            name: "ADT캡스",
        };
    },
    components: {
        header: Header,
        content: Content,
        footer: Footer,
    },
};
</script>

<style></style>