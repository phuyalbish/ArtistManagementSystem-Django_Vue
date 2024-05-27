<template>
    <div class="p-5 border border-blue-200 shadow-md shadow-blue-200">
        {{  albumItem.name }}
    </div>
</template>
<script>
export default{
    props:{
        albumItem:Object
    }
}
</script>