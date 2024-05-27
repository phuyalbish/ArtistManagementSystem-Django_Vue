<template>
    <form @submit.prevent="submitForm" class="form-container mt-10 flex gap-5">
      <input v-model="musicData.name" placeholder="Enter music name" class="input-field p-2" />
      <select v-model="musicData.album" class="select-field p-2">
        <option value="">Select Album</option>
        <option v-for="album in userAlbum" :key="album.id" :value="album.id">{{ album.name }}</option>
      </select>
      <button type="submit" class="submit-button" @click="sendData">Submit</button>
    </form>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default{
    data(){
        return {
            musicData:{
                name:"",
                album:"",
                artist: localStorage.getItem('userId')
            }
        }
    },
    computed:{

      ...mapState(['userAlbum'])
    },
    methods:{
    ...mapActions(['addData']),
    sendData(){
        console.log(this.musicData)
        this.addData(this.musicData)
    },
    }
}
</script>