<template>
  <PageLayout id="display-flex">
    <template #content>
      <div class="dashboard-container w-full">

          <MusicTiles/>

      </div>
    </template>
  </PageLayout>
</template>

<script>
import  MusicTiles from '../components/Tiles/MusicTiles.vue'
export default{
data(){
        return{
            id : this.$route.params.id
        }
    },
  components:{
    MusicTiles
  }

}

</script>