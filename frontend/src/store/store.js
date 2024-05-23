import { createStore } from "vuex";
export default createStore({
  state: {
    navbarState: "home",
    userData: Object,
    // access_token :localStorage.getItem("access_token"),
    // refresh_token : localStorage.getItem("refresh_token"),
  },
  mutations:{
    SET_USER_DATA(state, userData) {
    state.userData =  userData;
    },
  },
  actions:{
      setUserData({commit}, data ){
          commit('SET_USER_DATA', data)
      },


      // async getUserData(){
      //     if(this.access_token  && this.refresh_token){
      //         await axios.post(`${this.API}api/checkToken/`, {}, {
      //         headers: {
      //         "authorization": localStorage.getItem("access_token"),
      //         "content-Type": "application/json",
      //         }}).then(response =>{
      //             if(response.status == 200){
      //               // this.$store.userData = response.data.resData
      //               // store.commit('updateUserData', response.data.resData)
      //               this.setUserData(response.data.resData)
      //             }
      //       })
      //     }
      //     else{
      //       this.$router.push('/')
      //     }
      //   }
  },
  getters:{
    getUserData: state =>  state.userData
  }
});
