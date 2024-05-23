<script>
import axios from "axios";
import EditProfile from "./EditProfile.vue";
import TopPage from "@/components/EditUser.vue";
export default {
  components: { TopPage },
  data() {
    return {
      editShow: false,
      API: import.meta.env.VITE_BACKEND_API_URL,
      userData: [],
      userId: localStorage.getItem("userId"),
    };
  },
  mounted() {
    this.getData();
  },
  watch: {
    userData(newVal) {
      console.log("here", newVal);
      console.log(this.$store.userData);
    },
  },
  methods: {
    editClickOn() {
      this.editShow = true;
    },
    editClickOff() {
      this.editShow = false;
    },
    async getData() {
      await axios
        .get(`${this.API}api/user/getData/${this.userId}/`)
        .then((response) => {
          this.$store.userData = response.data;
          this.userData = response.data;
        });
    },
  },
};
</script>
<template>
  <div class="profile">
    <p><span class="name-text">Username: </span>{{ this.userData.username }}</p>
    <p><span class="name-text">FullName: </span>{{ this.userData.fullname }}</p>
    <p>
      <span class="name-text">Address: </span>{{ this.userData.city_id }},
      {{ this.userData.country_id }}
    </p>
    <p><span class="name-text">Email: </span>{{ this.userData.email }}</p>
    <div class="editAndDeleteButton">
      <div class="editButton" @click="editClickOn">Edit</div>
      <!-- <div class="deleteButton" @click="editClickOn">Delete</div> -->
    </div>
  </div>

  <TopPage
    class="EditProfile"
    v-show="editShow === true"
    @editShow="editClickOff"
    :userdetail="userData"
  />
</template>
<style>
h1 {
  color: #fff;
}
.EditProfile {
  position: absolute;
  top: 0px;
  width: 80vw;
}

.outerProfile {
  width: 100%;
  height: 100%;
  border: 1px solid red;
  width: 200px;
  padding: 10px;
  text-align: center;
}
.profile {
  width: 100%;
  height: 100vh;
  padding: 20px;
  border: 1px solid red;
  text-align: center;
  display: flex;
  gap: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.editAndDeleteButton {
  display: flex;
}
.editButton,
.deleteButton {
  width: 100px;
  margin: 5px;
  padding: 10px;
  color: #fff;
  border-radius: 10px;
  background-color: blue;
}
.editButton {
  background-color: blue;
}
.deleteButton {
  background-color: red;
}
.name-text {
  font-size: 20px;
  color: grey;
}
p {
  font-size: 19px;
}
</style>
