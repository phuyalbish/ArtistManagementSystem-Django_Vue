<script>
// import axios from "axios";
// import store from "@/store/store";
// import { mapGetters } from "vuex";
import Profile from '../pages/Profile.vue'
export default {
  components: {},
  props:[
      'user'
  ],
  data() {
    return {
      userData:"",
      articleData:"",
      searchName: "",
      is_openPopupSideBar: false,
      is_showSearchPopUp: false,
    };
  },

computed:{
//  getData(){
//     return store.getters.getUserData
//  }
},
  watch: {
    getData(newVal){
        this.userData = newVal.resData
    },
    searchName(newVal) {
      if (newVal == "") {
        this.is_showSearchPopUp = false;
      } else {
        this.is_showSearchPopUp = true;
        console.log(newVal);
      }
    },
  },
  methods: {
    logOut(){
         localStorage.removeItem("refresh_token");
         localStorage.removeItem("access_token");
         this.$router.push('/')
    },
    searchArticles() {
      console.log(this.searchName);
    },
    offFocusSearchBar() {
      this.is_showSearchPopUp = false;
    },
    onFocusSearchBar() {
      if (this.searchName != "") {
        this.is_showSearchPopUp = true;
      }
    },
    openClosePopupSideBar() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = !this.is_openPopupSideBar;
    },
  },
};
</script>
<template>
  <div
    class="header flex flex-wrap gap-4 items-center p-5 justify-between sm:justify-evenly"
  >
    <RouterLink to="/dashboard" class="headerTitleAndTag flex flex-col align-middle">
      <div class="headerTitle text-2xl text-blue-900 font-mono">
        Musica
      </div>
      <div class="headerTag text-xs text-slate-500">
        Place for music
      </div>
    </RouterLink>

    <div
      class="hidden bg-white text-sm sm:flex searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400"
    >
      <input
        type="text"
          size="21"
        class="outline-none px-4 bg-transparent"
        placeholder="Search Music, Album or Artist"
        v-model="searchName"
        @blur="offFocusSearchBar"
        @focus="onFocusSearchBar"
      />
      <p class="p-2">&#128269;</p>
    </div>



    <RouterLink to="/music" class="cursor-pointer   text-sm text-blue-900 hover:text-blue-500 hidden sm:flex">Musics</RouterLink>
    <RouterLink to="/artist" class=" cursor-pointer text-sm  text-blue-900 hover:text-blue-500 hidden sm:flex">Artists</RouterLink>
    <RouterLink to="/album" class=" cursor-pointer  text-sm  text-blue-900 hover:text-blue-500 hidden sm:flex">Albums</RouterLink>
    
    
    <div
      class="threeBar text-2xl text-blue-900 cursor-pointer select-none"
      @click="openClosePopupSideBar"
    >  
        <button type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
        
        <img class="h-8 w-8 rounded-full" src="../assets/default_profile.png" alt="">
        </button>
    </div>
    <div
      v-if="is_showSearchPopUp"
      class="z-20 searchField absolute top-36 z-2 w-5/6 h-20 sm:top-24 border rounded-lg shadow-md bg-white shadow-blue-400"
    ></div>
    
    <div v-if="is_openPopupSideBar" class="flex flex-row items-center gap-4 z-10 p-5 popUpSidebar absolute top-24 right-10 border b rounded-lg shadow-md shadow-blue-400 bg-blue-100">

      <div class="leftSide flex flex-col gap-3">
        <div class="flex text-sm justify-between sm:hidden searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400">
        <input
          type="text"
          size="21"
          class="outline-none px-4 bg-transparent flex-grow"
          placeholder="Search Music, Album or Artist"
          v-model="searchName"
          @blur="offFocusSearchBar"
          @focus="onFocusSearchBar"
        />
        <p class="p-2">&#128269;</p>
      </div>

      <RouterLink to="/music" class="   text-sm sm:hidden inline-block  cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700">Musics</RouterLink>
      <RouterLink to="/artist" class="  text-sm sm:hidden inline-block  cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700">Artists</RouterLink>
      <RouterLink to="/album" class="   text-sm sm:hidden inline-block  cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700">Albums</RouterLink>
      <RouterLink to="/profile" class=" text-sm  cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700" role="menuitem" tabindex="-1" id="user-menu-item-0">Visit Profile</RouterLink>
      <RouterLink to="/login" class="   text-sm  cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-red-700 border-red-700"  @click="logOut" >LogOut</RouterLink>

   
    </div>
      </div>
  </div>
</template>
<style></style>
