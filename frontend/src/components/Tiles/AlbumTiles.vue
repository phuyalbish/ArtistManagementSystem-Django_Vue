<template>
    <div class="flex gap-4 flex-wrap flex-grow justify-center ">
    <AlbumTile v-for="x in albumData" class="p-5" :albumDetail="x"/>

    </div>

</template>


<script>
import { mapState } from 'vuex';
import AlbumTile from '../Tile/AlbumTile.vue'
export default{
    components:{
        AlbumTile
    },
    
    computed:{
        ...mapState(['albumData'])
    }
}

</script>