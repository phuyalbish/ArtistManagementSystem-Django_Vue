<template>
    
        <div class="text-sm my-5 ">Musics:</div>
    <div class="flex gap-2">
    <MusicTile v-for="x in userMusic" :musicDetail="x"/>


    </div>

</template>

<script>
import { mapState } from 'vuex';
import MusicTile from '../Tile/MusicTile.vue';
export default{
    components:{
        MusicTile
    },
  data(){
   return{  

   }
  },
  computed:{
      ...mapState(['userMusic'])
  },
  methods:{
  }
  
  
}
</script>