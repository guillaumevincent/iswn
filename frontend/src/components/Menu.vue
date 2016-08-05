<style scoped>
    #menu, #menu a {
        color: white;
    }

    #menu .navbar-red {
        background-color: #C31336;
    }
    .nav-item{
        cursor: pointer;
    }
</style>
<template>
    <div id="menu">
        <nav class="navbar navbar-red bg-faded">
            <div class="container">
                <a class="navbar-brand" href="/#!/">ISWN</a>
                <ul class="nav navbar-nav pull-xs-right">
                    <!--
                    <li class="nav-item">
                        <a class="nav-link" href="/#!/pricing/">Tarifs</a>
                    </li>
                    -->
                    <li class="nav-item" v-show="user.authenticated">
                        <a class="nav-link" @click.stop.prevent="logout()">
                            <i class="fa fa-sign-out" aria-hidden="true"></i>
                        </a>
                    </li>
                    <li class="nav-item" v-show="!user.authenticated">
                        <a class="nav-link" href="/#!/login/">Espace adhérent</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>
<script type="text/ecmascript-6">
    import auth from '../services/auth';
    import logging from '../services/logging';

    export default {
        data() {
            return {
                user: auth.user
            };
        },
        methods: {
            logout(){
                auth.logout();
                logging.success(this.$t('login.logoutMessage'));
                this.$router.go('/');
            }
        }
    }
</script>
