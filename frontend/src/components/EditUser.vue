<template>


  <div class="LoginInSignUp absolute z-50 flex flex-col items-center right-10 m-auto gap-4 p-10 md:w-6/6 border bg-blue-100 rounded-lg shadow-md shadow-blue-400">
      
      <div class="flex  w-full justify-between">
          <h3 class="text-2xl text-blue-900">Edit Account</h3>
            <div class="text-2xl text-blue-900 cursor-pointer" @click="toggleCloseEdit">
                &#x274c;
            </div>

      </div>

      <div class="imgEdit cursor-pointer hover:bg-blue-700  shadow-md shadow-blue-300 hover:shadow-blue-900 p-7 border border-blue-900 bg-blue-400 rounded-full text-white">Img</div>
      
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="userData.email"
        @blur="checkMailAvailabe" required
      />
      
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Full Name"
        v-model="userData.fname" required
      />
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Bio"
        v-model="userData.bio" required
      />
     
      
      <div class="genderField  flex gap-6 outline-none p-3 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900">
      <label for="male"><input
        type="radio"
        id="male"
        value="male"
        name="gender"
        selected="selected"
        v-model="userData.gender"
      /> 
       Male</label>  
      
      <label for="female">
       <input
        type="radio"
        id="male"
        value="female"
        name="gender" selected="selected"
        v-model="userData.gender"  
      /> 
       Female</label>
      </div>

      <input type="submit"
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="submitEditedData"  value="Edit Profile"
      >
      
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
</template>

<script>
import store from '@/store/store';
import axios from 'axios';
export default {
  components: {
  },
  emits: ["editShow"],
  
  data() {
    return {

      API: "http://127.0.0.1:8000/",
      userData:"",
      compareData:"",
      gender:"",
      is_changeData: false,
      is_errorMsgSet: false,
      is_errorOccured: "asda",
      errorMessage: "asd",
      changedData: {},
      checkAvailability: false,

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
        console.log(this.userData)
        this.compareData = newVal.resData
        this.gender = newVal.resData.gender
    },
  },

  methods: {
    closeModal() {
      this.showModal = false;
    },
    toggleCloseEdit() {
      this.$emit("editShow");
    },

    editProfile(){
       axios.post(`${this.API}api/updateProfile/`, {}, {
              headers: {
              "content-Type": "application/json",
              }}).then(response =>{
                  if(response.status == 200){
                      console.log(response.data)
                  }
            })
    },


  


    // async checkMailAvailabe(email) {

    //   if(this.userData.email != ""){
    //       await axios({
    //         method: "post",
    //         url: `${this.API}api/checkMailAvailable/`,
    //         headers: {
    //           "Content-Type": "application/json",
    //         },
    //         data: { checkEmailID: email },
    //       }).then((response) => {
    //         this.checkAvailability = response.data.availability;
    //       });
    // }
    // },
    
    submitEditedData() {

      console.log("work")
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      // FullName
      if (this.compareData.fname != this.userData.fname) {
        this.is_changeData = true;
        this.changedData.fname = this.userData.fname;
      }
      // Username
      if (this.userData.email != this.compareData.email) {
        this.is_changeData = true;
        this.changedData.username = this.userData.email;
      }
      // Email
      if (this.userData.email != this.compareData.email) {
        if (emailRegex.test(this.userData.email)) {
          console.log(this.checkAvailability);
          if (this.checkAvailability) {
            console.log("Valid");
            this.is_changeData = true;
            this.changedData.email = this.userData.email;
          } else {
            console.log("email already exists");
          }
        } else {
          console.log("invalid");
        }
      }
      if (this.is_changeData == true) {
        axios({
          method: "patch",
          url: `${this.API}api/user/editData/${this.userId}/`,
          headers: {
            "Content-Type": "application/json",
          },
          data: this.changedData,
        });
        console.log("atleast one data changed");
        this.toggleCloseEdit();
      } else {
        console.log("No Data Changed");
      }
      this.is_changeData = false;
    },

  },

    
};
</script>

<style>
</style>








<!-- 






<script>
import axios from "axios";
export default {
  data() {
    return {
      is_changeData: false,
      is_errorMsgSet: false,
      errorMessage: "",
      userId: localStorage.getItem("userId"),
      API: import.meta.env.VITE_BACKEND_API_URL,
      userData: [],
      changedData: {},
      checkAvailability: false,
    };
  },
  mounted() {
    this.getData();
  },
  updated() {
    this.checkMailAvailabe(this.userData.email);
  },
  methods: {
    async getData() {
      await axios
        .get(`${this.API}api/user/getData/${this.userId}/`)
        .then((response) => {
          this.userData = response.data;
        });
    },
    async checkMailAvailabe(email) {
      await axios({
        method: "post",
        url: `${this.API}api/user/checkMailAvailable/`,
        headers: {
          "Content-Type": "application/json",
        },
        data: { checkEmailID: email },
      }).then((response) => {
        this.checkAvailability = response.data.availability;
      });
    },
    submitEditedData() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      // FullName
      console.log(this.userdetail.fullname);
      console.log(this.userData.fullname);
      if (this.userData.fullname != this.userdetail.fullname) {
        this.is_changeData = true;
        this.changedData.fullname = this.userData.fullname;
      }
      // Username
      if (this.userData.username != this.userdetail.username) {
        this.is_changeData = true;
        this.changedData.username = this.userData.username;
      }
      // Email
      if (this.userData.email != this.userdetail.email) {
        if (emailRegex.test(this.userData.email)) {
          console.log(this.checkAvailability);
          if (this.checkAvailability) {
            console.log("Valid");
            this.is_changeData = true;
            this.changedData.email = this.userData.email;
          } else {
            console.log("email already exists");
          }
        } else {
          console.log("invalid");
        }
      }
      if (this.is_changeData == true) {
        axios({
          method: "patch",
          url: `${this.API}api/user/editData/${this.userId}/`,
          headers: {
            "Content-Type": "application/json",
          },
          data: this.changedData,
        });
        this.userdetail.fullname = this.userData.fullname;
        this.userdetail.username = this.userData.username;
        this.userdetail.email = this.userData.email;
        console.log("atleast one data changed");
        this.toggleCloseEdit();
      } else {
        console.log("No Data Changed");
      }
      this.is_changeData = false;
    },
    toggleCloseEdit() {
      this.$emit("editShow");
    },
  },
};
</script>

<template>
  <div class="Container">
    <form>
      <div class="close" @click="toggleCloseEdit">x</div>
      <input
        class="user_input_field"
        placeholder="Username"
        v-model.lazy="userData.username"
      />
      <input
        class="user_input_field"
        placeholder="FullName"
        v-model.lazy="userData.fullname"
      />
      <input
        class="user_input_field"
        placeholder="Email"
        v-model.lazy="userData.email"
      />
      <input
        class="user_input_field"
        placeholder="Country"
        v-model.lazy="userData.country_id"
      />

      <input
        class="user_input_field"
        placeholder="City"
        v-model.lazy="userData.city_id"
      />
      <input
        class="user_input_field"
        placeholder="Phone"
        v-model.lazy="userData.phone"
      />
      <input
        class="user_input_field"
        placeholder="Skills"
        v-model.lazy="userData.skills_id"
      />

      <input
        class="user_input_field"
        placeholder="Faculty"
        v-model.lazy="userData.faculty_id"
      />

      <input
        class="user_input_field"
        placeholder="Field"
        v-model.lazy="userData.field_id"
      />

      <input
        class="user_input_field"
        placeholder="Interest"
        v-model.lazy="userData.interest_id"
      />

      <input
        class="user_input_field"
        placeholder="Linkedin Link"
        v-model.lazy="userData.link"
      />

      <input
        class="user_input_field"
        placeholder="Image"
        v-model.lazy="userData.imgSrc"
      />

      <input
        class="submit"
        type="button"
        value="submit"
        @click="submitEditedData"
      />
    </form>
  </div>
</template>
<style>
.Container {
  position: absolute;
  background-color: cyan;
  padding: 50px;
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
}
.user_input_field {
  padding: 10px;
  background-color: #fff;
  border-radius: 10px;
  border: 1px solid grey;
}
.submit {
  background-color: blue;
  color: #fff;
  padding: 10px;
}
.close {
  padding: 10px 16px;
  border-radius: 10px;
  border-radius: 100%;
  position: absolute;
  top: 0px;
  right: 0px;
}
.close:hover {
  background-color: grey;
  color: #fff;
}
</style> -->