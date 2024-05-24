<template>
  <PageLayout id="display-flex">
    <template #content>
       <DetailCard  info="Album" :id="id"/>
    </template>
  </PageLayout>
</template>

<script>
import  DetailCard from '../components/Card/DetailCard.vue'
export default{
    data(){
        return{
            id : this.$route.params.id
        }
    },
  components:{
    DetailCard
  }

}

</script>