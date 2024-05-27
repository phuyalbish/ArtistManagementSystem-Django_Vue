<script>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios';
export default{
    data(){

    return {
        API: "http://127.0.0.1:8000/",
        access_token :localStorage.getItem("access_token"),
        userId :localStorage.getItem("userId"),
    }
  },
  mounted(){

      // this.$store.dispatch('setUserData'),
      // this.$store.dispatch('setMusicData'),
      // this.$store.dispatch('setAlbumData'),
      // this.$store.dispatch('setArtistData')
  },
    methods:{

       async getUserData(){
              await axios.get(`${this.API}api/getCSRFToken/`, {}, {
              headers: {
              "content-Type": "application/json",
              }}).then(response =>{
                  if(response.status == 200){
                   localStorage.setItem("csrf",response.data.token)
                  }
            })
          }
        }


        
    }

</script>

<template>
  <RouterView />
</template>
