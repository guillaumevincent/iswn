import Vue from 'vue';
import VueRouter from 'vue-router';
import VueI18n from 'vue-i18n';

import App from './app';
import IndexPage from './pages/index';
import LoginPage from './pages/login';
import Dashboard from './pages/dashboard';
import auth from './services/auth';
import locales from './locales';

Vue.use(VueI18n);
const browserLanguage = (navigator.language || navigator.browserLanguage).split('-')[0];
const lang = browserLanguage in locales ? browserLanguage : 'en';
Vue.config.lang = lang;
Object.keys(locales).forEach(lang => {
  Vue.locale(lang, locales[lang]);
});

Vue.use(VueRouter);
const router = new VueRouter();

router.map({
  '/': {
    component: IndexPage
  },
  '/login/': {
    component: LoginPage
  },
  '/app/': {
    component: Dashboard,
    authRequired: true
  }
});

auth.localStorage = localStorage;

router.beforeEach(transition => {
  auth.checkAuth()
    .then(() => {
      if (transition.to.path === '/') {
        transition.redirect('/app/');
      } else {
        transition.next();
      }
    })
    .catch(() => {
      if (transition.to.authRequired) {
        transition.redirect('/login/');
      } else {
        transition.next();
      }
    });
});

router.redirect({
  '*': '/'
});

router.start(App, 'app');
