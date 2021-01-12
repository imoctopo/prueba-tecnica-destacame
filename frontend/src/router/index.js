import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Drivers from "@/views/Drivers";
import DriverEditor from "@/views/DriverEditor";
import Passengers from "@/views/Passengers";
import Buses from "@/views/Buses";
import Routes from "@/views/Routes";
import BusEditor from "@/views/BusEditor";


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            breadcrumb: [
                {name: 'Home'},
            ]
        }
    },
    {
        path: '/drivers',
        name: 'Drivers',
        component: Drivers,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Drivers'}
            ]
        }
    },
    {
        path: '/drivers/:id',
        name: 'DriverEditor',
        component: DriverEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Drivers', link: '/drivers'},
                {name: 'Editor'}
            ]
        }
    },
    {
        path: '/passengers',
        name: 'Passengers',
        component: Passengers,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Passengers'}
            ]
        }
    },
    {
        path: '/buses',
        name: 'Buses',
        component: Buses,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Buses'}
            ]
        }
    },
    {
        path: '/buses/:id',
        name: 'BusEditor',
        component: BusEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Buses', link: '/buses'},
                {name: 'Editor'}
            ]
        }
    },
    {
        path: '/routes',
        name: 'Routes',
        component: Routes,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Routes'}
            ]
        }
    }
];

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});