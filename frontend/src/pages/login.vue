<template>
    <div class="vignes">
        <div class="container">
            <div class="col-sm-8 offset-sm-2 col-lg-6 offset-lg-3 p-t-7">
                <div class="card card-block p-y-2">
                    <h4 class="card-title">ISWN: Se Connecter</h4>
                    <form v-on:submit.prevent="login" name="loginForm">
                        <fieldset class="form-group">
                            <p class="text-muted">
                                {{{ $t('login.LogInInfo') }}}
                            </p>
                            <label for="email" class="sr-only">{{ $t('login.Email') }}</label>

                            <input type="text" class="form-control" id="email" name="email"
                                   placeholder="{{ $t('login.EmailPlaceholder') }}"
                                   v-model="user.email" autofocus>
                        </fieldset>
                        <fieldset class="form-group">
                            <label for="password" class="sr-only">{{ $t('login.Password') }}</label>

                            <input type="password" class="form-control" id="password"
                                   v-model="user.password" name="passwordField"
                                   placeholder="{{ $t('login.PasswordPlaceholder') }}">
                        </fieldset>
                        <button id="buttonSubmit" name="buttonSubmit" type="submit" class="btn btn-success btn-block">
                            {{ $t('login.SignIn') }}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script type="text/ecmascript-6">
    import auth from '../services/auth';
    import logging from '../services/logging';

    export default {
        data() {
            return {
                user: {
                    email: '',
                    password: ''
                }
            };
        },
        methods: {
            login(){
                if (!this.user.email || !this.user.password) {
                    logging.error(this.$t('login.emailAndPasswordMandatory'));
                    return;
                }
                auth.login(this.user)
                        .then(()=> {
                            logging.success(this.$t('login.welcome'));
                            this.$router.go('/app/');
                        })
                        .catch(() => {
                            logging.error(this.$t('login.credentialsInvalids'));
                        });
            }
        }
    }
</script>

