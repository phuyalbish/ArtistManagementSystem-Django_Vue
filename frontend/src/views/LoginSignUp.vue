<template>
    <div class=" flex  justify-center mt-5 align-middle">

    <div
      v-if="is_shownLoginForm"
      class="LoginInSignUp z-50 flex flex-col items-center m-10 gap-4 p-10 md:w-4/6 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">Login to an Account</h3>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="loginData.email"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="loginData.password"
      />
      <p
        class="text-blue-900 cursor-pointer underline underline-offset-1"
        @click="ToggleSignUpDiv"
      >
        Create a new account
      </p>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="LoginSubmit"
      >
        Login
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>

    <div
      v-if="!is_shownLoginForm"
      class="LoginInSignUp z-50 flex flex-col items-center m-10 gap-4 p-10 md:w-4/6 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">Create New Account</h3>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="signUpData.email"
      />

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Full Name"
        v-model="signUpData.fname"
      />
      
      <textarea class="outline-none p-2 resize-none flex-grow rounded-md overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        id="w3review" name="w3review" rows="3" cols="25"
         placeholder="Bio"
        v-model="signUpData.bio"></textarea>
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="signUpData.password"
        @focus="validatePassword"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="re-type Password"
        v-model="signUpData.repassword"
      />
      <div class="genderField  flex gap-6 outline-none p-3 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900">
              <label for="male"><input
        type="radio"
        id="male"
        value="Male"
        name="gender"
        v-model="signUpData.gender"
      /> 
       Male</label>  
      
      <label for="female">
       <input
        type="radio"
        id="male"
        value="Female"
        name="gender"
        selected="selected"
        v-model="signUpData.gender" 
      /> 
       Female</label>
      </div>

         
      <p
        class="text-blue-900 cursor-pointer underline underline-offset-1"
        @click="ToggleLoginDiv"
      >
        Already have an account?
      </p>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="RegisterSubmit"
      >
        SignUp
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
    </div>
</template>
<script>
// const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!])(?=.*[^\w\d\s]).{8,}$/;
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { mapActions } from 'vuex';
export default{
        data(){
            return {
                access_token :localStorage.getItem("access_token"),
                refresh_token :localStorage.getItem("refresh_token"),
                API: "http://127.0.0.1:8000/",
                is_errorOccured : "",
                is_shownLoginForm :true,
                loginData: {
                    email: "",
                    password: "",
                },
                signUpData: {
                    email: "",
                    password: "",
                    repassword:"",
                    fname:"",
                    bio:"",
                    link:"",
                    gender:"Male",
                    // img_src:"",

                },
            }
        },
        mounted(){
            if(this.refresh_token & !this.access_token){
                axios.post(`${this.API}api/token/refresh/`, {'refresh': localStorage.getItem("refresh_token")}, {
                headers: {
                "content-Type": "application/json",
                }}).then(response =>{
                    if(!this.access_token){
                        localStorage.setItem("refresh_token",response.data.refresh);
                        localStorage.setItem("access_token",response.data.access);
                        let data = jwtDecode(response.data.access)
                        console.log(data.user_id)
                        localStorage.setItem("userId", data.user_id)
                    }
                    if(response.status == 200){
                        this.$router.push('/dashboard')
                    }
                })
            }
        },
        watch:{
          gender(){
              console.log(this.signUpData.gender)
          }
        },

         methods: {
            LoginSubmit() {

              if(this.loginData.email && this.loginData.password){
                
                axios
                  .post(`${this.API}api/token/`, this.loginData, {
                    headers: {
                    "content-Type": "application/json",
                    },
                  })
                  .then((response) => {
                  if(response.status == 200){
                      localStorage.setItem("refresh_token",response.data.refresh);
                      localStorage.setItem("access_token",response.data.access);
                      let data = jwtDecode(response.data.access)
                        localStorage.setItem("userId", data.user_id)
                    console.log(data.user_id)
                       this.$store.dispatch('setUserData')
                      this.$router.push('/dashboard')
                  }
                  else if(response.status == 401){
                    this.is_errorOccured = response.detail
                  }
                  })
                  .catch(error => {
                      // if(error){
                        this.is_errorOccured = error.response.data.detail
                      // }
                  })
                }
                else{
                    this.is_errorOccured = "Field is required"
                }



        
    },


    RegisterSubmit() {
      axios({
        method: "post",
        url: `${this.API}api/user/add/`,
        headers: {
          "Content-Type": "application/json",
        },
        data: this.signUpData,
      }).then(response => {
        console.log(response)
        if(response.status == 200){
              axios.post(`${this.API}api/token/`,{
                'email':this.signUpData.email,
                'password': this.signUpData.password
              }, {
                    headers: {
                    "content-Type": "application/json",
                    },
                  })
                  .then((response) => {
                  if(response.status == 200){
                      localStorage.setItem("refresh_token",response.data.refresh);
                      localStorage.setItem("access_token",response.data.access);
                      let data = jwtDecode(response.data.access)
                        localStorage.setItem("userId", data.user_id)
                    console.log(data.user_id)
                       this.$store.dispatch('setUserData')
                      this.$router.push('/dashboard')
                  }
                  else if(response.status == 401){
                    this.is_errorOccured = response.detail
                  }
                  })
                  .catch(error => {
                        this.is_errorOccured = error.response.data.detail
                      
                  })

        }
      }).catch(err => {
        console.log(err.response.data)
      this.is_errorOccured = err.response.data;
      });
    },
    ToggleLoginDiv() {
      this.is_errorOccured = "";
      this.is_shownLoginForm = true;
    },
    ToggleSignUpDiv() {
      this.is_errorOccured = "";
      this.is_shownLoginForm = false;
    },
}

}
</script>