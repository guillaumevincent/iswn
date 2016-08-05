<style>
    * {
        border-radius: 0 !important;
    }

    html, body, #app {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
    }

    .vignes {
        height: calc(100% - 54px);
        background: url('images/vignes-bg.jpg') no-repeat center center fixed;
        background-size: cover;
    }
    @media (min-width: 991px) {
        .p-t-7 {
            padding-top: 7em;
        }
    }
</style>
<template>
    <div id="app">
        <menu></menu>
        <router-view></router-view>
    </div>
</template>
<script type="text/ecmascript-6">
    import 'bootstrap/dist/css/bootstrap.css';
    import 'font-awesome/css/font-awesome.css';
    import 'notie/dist/notie.css';
    import 'bootstrap/dist/js/bootstrap.js';
    import Menu from 'components/Menu';

    export default {
        components: {
            'menu': Menu
        }
    };
</script>
