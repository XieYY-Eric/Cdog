<script>
// import axios from "axios"
export default{
    name:"Signup",
    data() {
        return {
            name:"",
            email: "",
            password: ""
        };
    },
    methods:{
        async signUp(){
            console.log("name", this.name, "email: ", this.email, "password: ", this.password);

            //fetch user information
            // let link = `http://localhost:3000/users?email=${this.email}&password=${this.password}`
            // let result = await axios.get(link);
            // if (result.status == 200 && result.data.length > 0){
            //     localStorage.setItem("user-info", JSON.stringify(result.data));
            //     this.$router.push({ name: 'Home' });
            // }
            console.warn("signUp Clicked");
        }
    },
    mounted(){
        let user = localStorage.getItem('user-info');
        if (user){
            this.$router.push({name:"Home"});
        }
    }
}
</script>

<template>
    <!-- <img src="../assets/logo.svg" class="logo" /> -->
    <h1>Sign Up</h1>
    <div class="Register">
        <input type="text" v-model="name" placeholder="Enter Name" />
        <input type="text" v-model="email" placeholder="Enter Email" />
        <input type="password" v-model="password" placeholder="Enter Password" />
        <button v-on:click="signUp">signUp</button>
    </div>
</template>


<style>
.Register{
    background-color: aqua;
    justify-items: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 20px;
    padding-top: 20px;
    padding-bottom: 20px;
    border: solid 1px black;
}
.Register input{
    width: 200px;
    height: 30px;
    border: 1px solid black;
}
.Register button{
    width: 100px;
    height: 30px;
    border-radius: 25px;
    text-align: center;
    cursor: pointer;
}

.Register button:disabled {
  cursor: default;
  opacity: .3;
}

.Register button:hover {
  background-image: linear-gradient(#51A9EE, #147BCD);
  border-color: #1482D0;
  text-decoration: none;
}

.Register button:active {
  background-image: linear-gradient(#3D94D9, #0067B9);
  border-color: #006DBC;
  outline: none;
}

.Register button:focus {
  box-shadow: rgba(131, 192, 253, 0.5) 0 0 0 3px;
  outline: none;
}


</style>

