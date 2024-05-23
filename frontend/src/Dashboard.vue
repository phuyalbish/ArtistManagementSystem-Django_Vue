<script>
import PageLayout from "./PageLayout.vue";
import Header from "./components/Header.vue";
import Sidebar from "./components/Sidebar.vue";
import Body from "./pages/Body.vue";
import axios from "axios";
export default {
  components: {
    PageLayout,
    Header,
    Sidebar,
    Body,
    
  },
  data(){
    return {
      API: "http://127.0.0.1:8000/",
      userData:"",
      // access_token :localStorage.getItem("access_token"),
      // refresh_token : localStorage.getItem("refresh_token"),
    }
  },

  computed(){
     if(this.access_token  && this.refresh_token){
          axios.post(`${this.API}api/token/verify/`, {}, {
          headers: {
          // "Authorization": 'Bearer' + localStorage.getItem("access_token"),
          "content-Type": "application/json",
          }}).then(response =>{
              if(response.status == 200){
                console.log(response)
                this.$store.userData = response.data

              }
        })
      }
      else{
        this.$router.push('/')
      }
  }
};
</script>

<template>
  <PageLayout id="display-flex">
    <template #sidebar>
      <!-- <Sidebar class="" /> -->
    </template>
    <template #header>
      <Header :user="userData"/>
    </template>
    <template #content>
      <Body />
    </template>
  </PageLayout>
</template>

<style></style>
