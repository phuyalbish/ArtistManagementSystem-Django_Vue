<template>
    <div class="flex align-middle border flex-wrap gap-5 p-3 border-blue-300 rounded-md bg-blue-100 shadow-md shadow-blue-200">
        

   
        <div class="flex  justify-center flex-col md:flex-row align-middle  gap-5 ">
            <img src="../../assets/default_user.png" class="w-40 h-40  m-auto rounded-full  align-middle" alt="">
            <div class="flex flex-col gap-2 rounded-md align-middle  justify-center text-center sm:text-left ">
                <div class="text-3xl text-blue-900">
                {{ userData.fname }}
                </div>

                <div class="role flex gap-2 text-blue-600">
                    <div v-if="userData.is_artist" class="text-sm p-1 rounded-lg bg-blue-800 text-white">
                    Artist
                </div>

                <div v-if="userData.is_staff" class="text-sm p-1 rounded-lg bg-blue-800 text-white">
                    Staff
                </div>

                <div v-if="userData.is_superuser" class="text-sm p-1 rounded-lg bg-blue-800 text-white">
                    Admin
                </div>
                </div>
                <div class="text-sm text-blue-600">
                    {{ userData.bio }}
                    
                </div>
                <div class="text-sm text-blue-600">
                    {{ userData.email }}
                </div>
                <div class="total justify-center sm:justify-start flex">
                    <div class="text-sm text-blue-500  ">
                    <pre>{{userData.total_follower }} Follower </pre> 
                    </div>
                <div v-if="userData.is_artist" class="text-sm  justify-center sm:justify-start text-blue-500  ">
                    <pre>,{{userData.total_follower }} Musics, {{userData.total_follower }} Album </pre> 
                </div>
                </div>
                <div class="link justify-center sm:justify-start  flex gap-2">
                    &#128279; 
                <div class="text-sm text-blue-500 cursor-pointer underline">
                {{ userData.link }}
                </div>
                </div>
                <div class="flex align-middle justify-evenly sm:w-28 sm:justify-start">
                    <div class="edit text-sm cursor-pointer p-2 rounded-lg  m-auto bg-blue-800 text-white" @click="openEdit">Edit</div>
                <div class="edit text-sm cursor-pointer  p-2 rounded-lg  m-auto bg-red-800 text-white">Delete</div>
            
                </div>
            
            </div>
        
        </div>
        
    </div>
        
</template>
<script>
import { mapState } from 'vuex';
export default{
    emits: ["changeState"],
  data(){
   return{
    
   }
  },
  computed:{
      ...mapState(['userData'])
  },
  methods:{
    openEdit(){
        console.log("WHatt")
        this.$emit('changeState')
    }
  }
  
  
}
</script>