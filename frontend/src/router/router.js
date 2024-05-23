import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../Dashboard.vue";
import LoginSignUp from "../pages/LoginSignUp.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{ path: "/", component: LoginSignUp },
    {path: "/dashboard", component: Dashboard},
  ]
});

export default router;
