<script>
import axios from 'axios';
import ViewDetail from '../components/ViewDetail.vue'
export default{
    components:{
        ViewDetail,
    },
    data(){
        return {
            articleData: [],
            API: "http://127.0.0.1:8000/",
            viewDetail: false,
            articleDetail:"",
            email:"",
         };
        
    },
    
    mounted(){
        //   axios.get(`${this.API}api/articles/getAllArticle/`).then(response =>{
        //       console.log(response)
        //       this.articleData = response.data
        // })
      },
      methods:{
        // viewDetail(id){
           
        // }
        changeData(x){
            console.log(x)
            this.articleDetail= x
        },
        openDetail(){
            this.viewDetail = true
        },
        closeDetail(){
            this.viewDetail=false
        }
      }
}

</script>
<template>
     <div class="mt-10 articleContainer flex gap-5 flex-wrap flex-shrink">
     <ViewDetail v-if="viewDetail" :articleDetails="articleDetail" :useremail="email"  class="rounded-lg shadow-lg p-10 shadow-blue-600 flex md:ml-20 absolute w-5/6 h-5/6 bg-blue-100" @viewDetail="closeDetail"/>
   
        <div v-for="x in articleData" @click="openDetail" @mouseenter="changeData(x)" class="cursor-pointer flex flex-col flex-wrap gap-2 w-100 bg-blue-50 p-10 m-1 hover:p-11 hover:m-0 border rounded-lg shadow-md shadow-blue-400">
               
            <div class="flex justify-between" ><h2 class="text-2xl text-blue-900">{{x.title}}</h2>
                <div class="text-xs  bg-blue-500 p-2 rounded-xl text-white hover:text-blue-500 border hover:bg-white hover:border-blue-500">{{ x.categoryname }}</div>
            </div>
            <p class="text-sm text-blue-400">{{ x.description }}</p>
            <div class="otherDetail flex justify-between  pt-5 align-middle">
                        <div class="detail flex flex-col align-middle">
                        <p class="text-sm text-blue-900">19th May,  {{x.totalLikes}} likes </p>
                        <p class="text-sm">{{x.authorname}}</p>
                        </div>
                        <div class="cursor-pointer  text-black text-lg  border hover:border-black-500  rounded-full px-2 align-middle">&#x1F44D;</div>
            </div>

        </div>

    </div>
</template>
<style></style>
