import Home from"./components/Home.vue"
import Login from "./components/Login.vue"
import Signup from "./components/Signup.vue"
import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        name:"Home",
        component:Home,
        path:"/"
    },
    {
        name:"Login",
        component:Login,
        path:"/login"
    },
    {
        name:"Signup",
        component:Signup,
        path:"/signup"
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})


export default router