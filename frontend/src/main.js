import PageLayout from './PageLayout.vue'
import "./style.css";
import { createApp } from 'vue'
import App from './App.vue'
import router from './index'
import store from "./store/store.js";
const app = createApp(App)

app.use(router)
app.use(store)
app.component("PageLayout", PageLayout)
app.mount('#app')
