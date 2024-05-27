<template>
  <PageLayout id="display-flex">
    <template #content>
      <div class="flex gap-2 flex-wrap sm:flex-nowrap">

          <div v-if="showEdit" class="sidebar  h-auto w-full">
              <EditUser @changeState="closeEdit" class="z-0"/>
          </div>

          <div class="allother">

              <ProfileBanner class=""   @changeState="openEdit"/>

                <AddMusic/>
                <ProfileAlbum/>
                <ProfileMusic/>
          </div>
      </div>
    </template>
  </PageLayout>
</template>
<script>
import { mapState } from 'vuex';
import ProfileBanner from '../components/Profile/ProfileBanner.vue'
import EditUser from '../components/Edit/EditUser.vue'
import ProfileAlbum from '@/components/Profile/ProfileAlbum.vue';
import ProfileMusic from '@/components/Profile/ProfileMusic.vue';
import AddMusic from '@/components/Profile/Add/AddMusic.vue'
export default{
  components:{
    ProfileBanner,
     EditUser,
     ProfileAlbum,
     ProfileMusic,
     AddMusic
  },
  data(){
   return{
        showEdit: false
   }
  },

  mounted(){
      this.$store.dispatch('setUsersAlbum')
      this.$store.dispatch('setUsersMusic')
  },
  methods:{
    closeEdit(){
        this.showEdit = false
    },
    openEdit(){
      this.showEdit = true
    }
  }
  
  
}
</script>