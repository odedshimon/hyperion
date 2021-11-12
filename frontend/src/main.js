import axios from 'axios'
import VueRouter from 'vue-router'
import Vue from 'vue'

import Home from "./components/Home"
import App from './App.vue';

Vue.config.productionTip = false
Vue.prototype.$http = axios;
Vue.use(VueRouter);

// create a router instance
const router = new VueRouter({
    mode: 'history',
    base: __dirname,
    routes: [{
            path: '/',
            component: Home,
            name: 'home'
        },
    ]
});

// pass the router to the app config
new Vue({
    router: router,
    render: h => h(App),
}).$mount('#app');