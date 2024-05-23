<script>
import axios from "axios";
import TopPage from "./EditUser.vue";
import AddArticle from "./AddArticle.vue"
import store from "@/store/store";
import { mapGetters } from "vuex";

export default {
  components: {TopPage, AddArticle},
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
      editShow: false,
      addShow: false
    };
  },

computed:{
 getData(){
    return store.getters.getUserData
 }
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
    editClickOn() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = false;
      this.editShow = true;
    },

    editClickOff() {
      this.editShow = false;
    },
   addClickOn() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = false;
      this.editShow = false;
      this.addShow = true;
    },

    addClickOff() {
      this.addShow = false;
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
    <div class="headerTitleAndTag flex flex-col align-middle">
      <div class="headerTitle text-2xl text-blue-900 font-mono">
        MusicFolio
      </div>
      <div class="headerTag text-xs text-slate-500">
      place for the instrumental music
      </div>
    </div>

    <div
      class="hidden sm:flex searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400"
    >
      <input
        type="text"
        class="outline-none px-4 bg-transparent"
        size="23"
        placeholder="Search Musics, Artists, Albums"
        v-model="searchName"
        @blur="offFocusSearchBar"
        @focus="onFocusSearchBar"
      />
      <p class="p-2">&#128269;</p>
    </div>
    <div class="text-3xl cursor-pointer text-blue-900 rounded-full hover:border  px-2 hover:border-blue-900">+</div>
    <div
      class="threeBar text-2xl text-blue-900 cursor-pointer select-none"
      @click="openClosePopupSideBar"
    >  

    a
      {{userData.email }}
    </div>
    <div
      v-if="is_showSearchPopUp"
      class="z-20 searchField absolute top-36 z-2 w-5/6 h-20 sm:top-20 border rounded-lg shadow-md bg-white shadow-blue-400"
    ></div>
    
    <div v-if="is_openPopupSideBar" class="flex flex-row items-center gap-4 z-10 p-10 popUpSidebar absolute top-20 right-10 border b rounded-lg shadow-md shadow-blue-400 bg-blue-100">

      <div class="leftSide flex flex-col gap-3">
        <div class="flex justify-between sm:hidden searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400">
        <input
          type="text"
          class="outline-none px-4 bg-transparent flex-grow"
          placeholder="Search Musics, Artists, Albums"
          v-model="searchName"
          @blur="offFocusSearchBar"
          @focus="onFocusSearchBar"
        />
        <p class="p-2">&#128269;</p>
      </div>
      <div class="addArticle cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700" @click="addClickOn">Add Article</div>
      <div class="addProfile cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-blue-700 border-blue-700"  @click="editClickOn" >Edit Profile</div>
      <div class="addProfile cursor-pointer text-white border rounded-md px-5 py-2 hover:text-blue-900 hover:bg-transparent bg-red-700 border-red-700"  @click="logOut" >LogOut</div>
    </div>
      </div>
  </div>

  <AddArticle 
  v-show="addShow === true"
    @addShow="addClickOff"
    :articleData="articleData"
    />
  <TopPage
    class="EditProfile"
    v-show="editShow === true"
    @editShow="editClickOff"
    :userData="userData"
  />
</template>
<style></style>
