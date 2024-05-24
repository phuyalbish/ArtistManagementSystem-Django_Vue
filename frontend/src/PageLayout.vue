
<script>
import Header from './components/Header.vue';
export default{
  components:{
    Header
  }
}
</script>
<template>
  <div class="containerLayout h-screen flex flex-col">
    <div class="header fixed w-full shadow-md shadow-blue-300 bg-blue-50">
      <Header />
    </div>

      <div class="main-content my-32  w-5/6 mx-auto">
        <slot name="content" >

        </slot>
    </div>
  </div>
</template>
