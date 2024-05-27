import { createStore } from "vuex";
import axios from "axios";
const URL = "http://127.0.0.1:8000/";
export default createStore({
  state: {
    userData: Object,
    userAlbum: Object,
    userMusic: Object,
    musicData: Object,
    albumData: Object,
    artistData: Object
  },
  mutations:{
    SET_USER_DATA(state, userData) {
      state.userData =  userData;
    },
    SET_USER_ALBUM(state, userAlbum) {
        state.userAlbum =  userAlbum;
    },

    SET_USER_MUSIC(state, userMusic) {
        state.userMusic =  userMusic;
    },
    SET_MUSIC_DATA(state, musicData) {
        state.musicData =  musicData;
    },
    SET_ALBUM_DATA(state, albumData) {
        state.albumData =  albumData;
    },

    SET_ARTIST_DATA(state, artistData) {
        state.artistData =  artistData;
    },
    ADD_MUSIC(state, newData) {
      state.musicData.push(newData);
  },
    ADD_ALBUM(state, newData) {
      state.albumData.push(newData);
  }
  },
  actions:{
      setUserData({commit} ){
        const userId = localStorage.getItem("userId")
        axios.get(`${URL}api/user/get/${userId}/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token'),
            'Content-Type': 'application/json'
          }
        }).then((response) =>{
                commit('SET_USER_DATA', response.data)
            }
        )
      },
  setUsersAlbum({commit}){
    const userId = localStorage.getItem("userId")
        axios.get(`${URL}api/album/get/user/${userId}/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token')
          }
        }).then((response) =>{
                commit('SET_USER_ALBUM', response.data)
            }
        )
  },
  setUsersMusic({commit}){
    const userId = localStorage.getItem("userId")
        axios.get(`${URL}api/music/get/user/${userId}/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token')
          }
        }).then((response) =>{
                commit('SET_USER_MUSIC', response.data)
            }
        )
  },




  setMusicData({commit}){
        axios.get(`${URL}api/music/get/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token')
          }
        }).then((response) =>{
                commit('SET_MUSIC_DATA', response.data)
            }
        )
  },

  setAlbumData({commit}){
        axios.get(`${URL}api/album/get/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token')
          }
        }).then((response) =>{
                commit('SET_ALBUM_DATA', response.data)
            }
        )
  },



  setArtistData({commit}){
        axios.get(`${URL}api/user/get/`, {
          headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token')
          }
        }).then((response) =>{
                commit('SET_ARTIST_DATA', response.data)
            }
        )
  },

  async addData({ commit }, newData) {
      try {
        const userId = localStorage.getItem("userId")
        await axios.post(`${URL}api/music/add/`, newData,{
         headers:{
            Authorization: "Bearer "+localStorage.getItem('access_token'),
            'Userid': userId
          }
        }).then((response) =>{
                commit('ADD_MUSIC', response.data);
        })
        
      } catch (error) {
        console.error('Error adding data:', error);
      }
    }





  },
  getters:{
    getUserData: state =>  state.userData
  }
});


