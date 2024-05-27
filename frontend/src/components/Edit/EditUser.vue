<template>

    <div
      class="w-full  top-24 m-auto border bg-white p-2 rounded-lg shadow-md shadow-blue-400"
    >
    <div class="relative flex flex-col  items-center  gap-4">
        <!-- <div class="nothing">as</div> -->
            <div class="text-2xl absolute top-2 left-2 text-blue-900 cursor-pointer" @click="closeEdit">X</div>
      <input
        type="text"
        class="outline-none mt-10 p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
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
        name="gender" selected="selected"
        v-model="signUpData.gender" 
      /> 
       Female</label>
      </div>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="EditSubmit"
      >
        Edit
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>


    </div>
      
    </div>
</template>

<script>
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { mapActions } from 'vuex';
export default{
    emits:['changeState'],
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
        methods:{
                EditSubmit(){
                    console.log("Whattt")
                },
                closeEdit(){
                    this.$emit('changeState')
                }
        }

    }

</script>