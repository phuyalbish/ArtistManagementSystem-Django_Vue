import PageLayout from './PageLayout.vue'
import "./style.css";
import { createApp } from 'vue'
import App from './App.vue'
import router from './index'
const app = createApp(App)

app.use(router)
app.component("PageLayout", PageLayout)
app.mount('#app')
