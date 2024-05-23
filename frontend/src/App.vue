<script>
import Dashboard from "./Dashboard.vue";
import Home from "./Home.vue";
import LoginSignUp from "./pages/LoginSignUp.vue";
import axios from "axios";
import store from "./store/store";
import { mapActions } from "vuex";
export default {
  components: {
    LoginSignUp,
    Dashboard,
    Home
    
  },
  data(){
      return {
        API: "http://127.0.0.1:8000/",
        userData:"",
        access_token :localStorage.getItem("access_token"),
        refresh_token : localStorage.getItem("refresh_token"),
      }
  },

  mounted(){
      this.getUserData()
    },
    methods:{

        ...mapActions(['setUserData']),
       async getUserData(){
        console.log(this.access_token)
          if(this.access_token  && this.refresh_token){
              await axios.get(`${this.API}api/user/get/`, {}, {
              headers: {
              "Authorization": this.access_token,
              "content-Type": "application/json",
              // "Userid": localStorage.getItem('Userid')
              }}).then(response =>{
                  if(response.status == 200){
                    store.commit('SET_USER_DATA',response.data)
                  }
            })
          }
          else{
            this.$router.push('/')
          }
        }
    }

};
</script>

<template>
  <router-view/>
</template>

<style></style>
