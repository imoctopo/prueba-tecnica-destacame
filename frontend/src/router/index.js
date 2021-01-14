import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Rides from "@/views/Rides";
import RideEditor from "@/views/RideEditor";
import Routes from "@/views/Routes";
import RouteEditor from "@/views/RouteEditor";
import Drivers from "@/views/Drivers";
import DriverEditor from "@/views/DriverEditor";
import Buses from "@/views/Buses";
import BusEditor from "@/views/BusEditor";
import Passengers from "@/views/Passengers";
import PassengerEditor from "@/views/PassengerEditor";
import TicketEditor from "@/views/TicketEditor";


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
        path: '/rides',
        name: 'Rides',
        component: Rides,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Rides'}
            ]
        }
    },
    {
        path: '/rides/:id',
        name: 'RideEditor',
        component: RideEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Rides', link: '/rides'},
                {name: 'Editor'}
            ]
        }
    },
    {
        path: '/rides/:rideId/tickets/:id',
        name: 'TicketEditor',
        component: TicketEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Rides', link: '/rides'},
                {name: 'rideId', link: '/rides/'},
                {name: 'New Ticket'}
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
        path: '/passengers/:id',
        name: 'PassengerEditor',
        component: PassengerEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Passengers', link: '/passengers'},
                {name: 'Editor'}
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
    },
    {
        path: '/routes/:id',
        name: 'RouteEditor',
        component: RouteEditor,
        meta: {
            breadcrumb: [
                {name: 'Home', link: '/'},
                {name: 'Routes', link: '/route'},
                {name: 'Editor'}
            ]
        }
    }
];

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});