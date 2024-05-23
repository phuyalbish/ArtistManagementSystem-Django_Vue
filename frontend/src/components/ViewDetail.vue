<template>
    <div class=" flex flex-col gap-3" >
        <div class="topbar flex gap-3 align-middle">
            <div class="goback text-3xl cursor-pointer text-blue-900" @click="closeDetail">&#8592;</div>
            <div class="flex flex-col">

            <div class="title text-3xl text-blue-900">{{ articleDetails.title }}</div>
            <div class="text-sm text-blue-500">{{articleDetails.description}}</div>
            </div>
        </div>
        <p class="text-gray-700">Lorem ipsum dolor sit amet consectetur Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione quam, sit odit dolore aliquid minus veniam natus nobis. Excepturi volulorem Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae est deserunt veniam voluptates corporis maxime reprehenderit, quibusdam quos distinctio doloribus quidem, voluptatem quod corrupti laboriosam enim, modi dolorem ducimus ab.ptas quae fuga cupiditate consequuntur obcaecati voluptatem eos sunt. Voluptatem, aliquid?, adipisicing elit. Itaque, veniam debitis! Ducimus vitae veritatis in eaque debitis magnam numquam iste, nostrum minima eveniet distinctio sapiente possimus. Maxime optio non mollitia?Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis harum dolorum ipsam porro facere tempore? Impedit, amet sit ad voluptatibus nulla deleniti, temporibus sunt totam commodi id autem voluptates illum?</p>
        <div class="profile flex justify-between align-middle ">
            <div class="flex  gap-2" >
               <div class="text-2xl cursor-pointer  text-black  border hover:border-black-500  rounded-full px-2 align-middle">&#x1F44D;</div>
                <p>{{articleDetails.totalLikes}} Likes</p>
            </div>

            <div v-if="articleDetails.authorname == compareEmail" class="flex gap-2">
                <div class="bg-blue-700 cursor-pointer rounded-2xl h-10 p-2 px-4 text-white hover:bg-white hover:text-blue-900 border border-blue-700">Edit</div>
                <div class="bg-red-700 cursor-pointer rounded-2xl h-10 p-2 px-4 text-white  hover:bg-white hover:text-red-900 border border-red-700">Delete</div>
            </div>
            <div class="flex gap-2">
                <div class="flex flex-col justify-end ">
                    <div class="text-md">{{articleDetails.authorname}}</div>
                    <div class="text-sm text-gray-500 border text-right">{{articleDetails.categoryname}}</div>
                </div>
                <div class="border border-blue-900  rounded-full w-12 h-12"></div>
            </div>
        </div>
        <div class="Comment flex border flex-shrink-0 border-blue-300 rounded-lg overflow-hidden align-middle">
            <input type="text" class="w-full outline-none py-2 px-5  " placeholder="Write Your Comment">
            <div class="text-gray-600 py-3 px-5 cursor-pointer">Post</div>
        </div>
        <div class="allComment">
            <p class="text-sm text-gray-700 cursor-pointer hover:text-gray-900">View All {{articleDetails.totalcomments}} Comment ></p>
        </div>
    
    </div>
</template>

<script>

import store from '@/store/store';
        export default{
            emits: ['viewDetail'],
            props: {
                articleDetails:"",
        },
        computed:{
                getData(){
                    return store.getters.getUserData
                }
            },
            data(){

                return {
                    compareEmail : ""
                }
            },
            watch: {
                getData(newVal){
                    // this.article.authorid = newVal.resData.id
                    console.log("************888")
                    console.log(newVal.resData.email)
                    this.compareEmail = newVal.resData.email
                }
            },
        mounted(){
            console.log(this.compareEmail)
            console.log(this.articleDetails.authorname)
        },
            methods:{
                    closeDetail() {
                    this.$emit("viewDetail");
                    },
            
            },

            
        }
</script>