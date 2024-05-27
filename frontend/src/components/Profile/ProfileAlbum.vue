<template>
        <div class="text-sm my-5 ">Albums:</div>
    <div class="flex gap-2">
<AlbumTile v-for="x in userAlbum" :albumDetail="x"/>


    </div>

</template>

<script>
import { mapState } from 'vuex';
import AlbumTile from '../Tile/AlbumTile.vue';
export default{
    components:{
        AlbumTile
    },
  data(){
   return{  

   }
  },
  computed:{
      ...mapState(['userAlbum'])
  },
  methods:{
  }
  
  
}
</script>