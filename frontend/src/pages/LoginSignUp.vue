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
        @click="getAPI"
      >
        Login
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>

    <div
      v-if="is_shownSignUpForm"
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
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="signUpData.password"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="re-type Password"
      />
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Full Name"
        v-model="signUpData.fname"
      />

       <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Bio"
        v-model="signUpData.bio"
      />

       <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Link"
        v-model="signUpData.link"
      />
      
      <div class="genderField  flex gap-6 outline-none p-3 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900">
              <label for="male"><input
        type="radio"
        id="male"
        value="male"
        name="gender"
        v-model="signUpData.gender"
      /> 
       Male</label>  
      
      <label for="female">
       <input
        type="radio"
        id="male"
        value="female"
        name="gender" selected="selected"
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
const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!])(?=.*[^\w\d\s]).{8,}$/;
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { errorMessages } from 'vue/compiler-sfc';
export default{
        data(){
            return {
                access_token :localStorage.getItem("access_token"),
                refresh_token :localStorage.getItem("refresh_token"),
                API: "http://127.0.0.1:8000/",
                is_errorOccured : "",
                is_shownSignUpForm : false,
                is_shownLoginForm :true,
                is_LoggedIn: false,
                loginData: {
                    email: "",
                    password: "",
                },
                signUpData: {
                    email: "",
                    password: "",
                    fname:"",
                    bio:"",
                    link:"",
                    gender:"Male",
                    img_src:"default.jpg",

                },
            }
        },
        mounted(){
          console.log("loaded")

            if(this.refresh_token){
              console.log(this.refresh_token)
                axios.post(`${this.API}api/token/refresh/`, {"refresh": this.refresh_token}, {headers:{"content-Type": "application/json", }})
                .then((response) => {
                    console.log(response)
                  if(response.status == 200){
                      localStorage.setItem("access_token",response.data.access);
                      this.$router.push('/dashboard')
                      this.is_LoggedIn = true
                  }
                  }).catch(error => {
                        this.is_errorOccured = error.response.data.detail
                  })
            }
            else{
                console.log("No Token Found!")
                this.$router.push('/')
            }

          console.log("loadeddasd")
        },

         methods: {



            async getAPI(){
              if(this.loginData.email && this.loginData.password){
                await axios.post(`${this.API}api/token/`, this.loginData, {headers:{"content-Type": "application/json", }})
                .then((response) => {
                    console.log(response)
                  if(response.status == 200){
                      localStorage.setItem("refresh_token",response.data.refresh);
                      localStorage.setItem("access_token",response.data.access);
                      let data = jwtDecode(response.data.access)
                      localStorage.setItem("Userid", data.user_id)
                      this.$router.push('/dashboard')
                      this.is_LoggedIn = true
                  }
                  }).catch(error => {
                        this.is_errorOccured = error.response.data.detail
                  })
                }
                else{
                   this.is_errorOccured="Fields are required"
                }

            },

    RegisterSubmit() {
      if(this.loginData.email != "" && this.loginData.password != ""){
        axios.post(`${this.API}api/user/add/`,JSON.stringify(this.signUpData) , {
            headers: {
            "content-Type": "application/json",
            }
          }).then(response => {
          if(response.status == 200){
              console.log(response)
              axios.post(`${this.API}api/token/`, {"email": this.signUpData.email, "password": this.signUpData.password }, {headers:{"content-Type": "application/json", }})
              .then((response) => {
                  console.log(response)
                if(response.status == 200){
                    localStorage.setItem("refresh_token",response.data.refresh);
                    localStorage.setItem("access_token",response.data.access);
                      let data = jwtDecode(response.data.access)
                      localStorage.setItem("Userid", data.user_id)
                    this.is_LoggedIn = true
                    this.$router.push('/dashboard')
                }
                }).catch(error => {
                      this.is_errorOccured = error.response
                })
            }
          }).catch(err => {
            console.log(err.response)
          });
      }
      else{
        this.is_errorOccured="Fields are required"
      }
    },


    ToggleLoginDiv() {
      this.is_shownSignUpForm = false;
      this.is_errorOccured="";
      this.is_shownLoginForm = !this.is_shownLoginForm;
    },
    ToggleSignUpDiv() {
      this.is_shownLoginForm = false;
      this.is_errorOccured="";
      this.is_shownSignUpForm = !this.is_shownSignUpForm;
    },
}

}
</script>