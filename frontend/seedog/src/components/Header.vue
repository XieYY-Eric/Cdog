<script>
export default{
    name:"Header",
    methods:{
        logout(){
            console.warn("logOut now");
            localStorage.removeItem("user-info");
            this.$router.push({ name: "Login"});
        }
    }
}
</script>

<template>
    <div class="nav">
        <router-link to="/">Home</router-link>
        <router-link to="/">Gallery</router-link>
        <router-link to="/">View</router-link>
        <a v-on:click="logout" href="#">Logout</a>
    </div>
</template>

<style>
.nav{
    background-color: black;
    overflow: scroll;
    border: solid 1px black;
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.nav a{
    float: left;
    color: #f2f2f2f2;
    padding: 16px;
    text-align: center;
    font-size: 17px;
    text-decoration: none;
    margin-right: 5px;
}
a:hover {
    background: #ddd;
    color: #333;
}
</style>