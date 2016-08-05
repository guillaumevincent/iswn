<style scoped>
    @media (min-width: 991px) {
        .p-t-7 {
            padding-top: 7em;
        }
    }
</style>
<template>
    <div class="vignes">
        <div class="container">
            <div class="col-sm-8 offset-sm-2 col-lg-6 offset-lg-3  p-t-7">
                <div class="p-y-2">
                    <h2 class="display-5">
                        Codes Uniques Pour Le Vin
                    </h2>
                    <p class="lead">
                        Récupérez des informations fiables de manière simple sur les produits viticoles que vous
                        manipulez
                    </p>
                    <form>
                        <div class="form-group">
                            <input type="text" class="form-control" id="formGroupExampleInput"
                                   placeholder="Recherchez un vin">
                        </div>
                    </form>
                </div>
            </div>
        </div>
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

