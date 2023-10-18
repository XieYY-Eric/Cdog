<script>
import Header from './Header.vue';
// import axios from "axios";
export default{
    name:"Home",
    components:{
        Header
    },
    data(){
        return{
            username:"",
            image:null,
            result_data:"None"
        }
    },
    mounted(){
        let user = localStorage.getItem('user-info');
        if (!user){
            this.$router.push({name:"Login"});
        }else{
            console.log(user)
            if(JSON.parse(user)){
            this.username = JSON.parse(user).email;
            }
            
        }
    },
    methods:{
        selectImage() {
        // Trigger the file input when the button is clicked
        this.$refs.fileInput.click();
        },

        async handleFileChange(event) {
            try{
                const file = event.target.files[0];

                if (file && file.type.startsWith('image/')) {
                    // If the selected file is an image, store it in the "image" variable
                    this.image = URL.createObjectURL(file);
                    // now send the image to frontend
                    const targeturl = "http://127.0.0.1:5000/upload";
                    
                    const formData = new FormData();
                    formData.append('file', file);
                    fetch(targeturl, {
                        method: 'POST',
                        body: formData
                        }).then(response => response.json())
                        .then(data => {this.result_data=data.result})
                    // let result = await axios.post(targeturl,formData);
                    // console.warn(result);
                } else {
                    // Handle non-image files or no file selected
                    this.image = null;
                    alert('Please select a valid image file.');
                }
            }catch(e) {
                console.log(e);
            }
            
        }
    }
}
</script>

<template>
<Header></Header>
<!-- <h1>This is Home Page</h1> -->
<div class="greeting">
    <p style="font-size:1cm;
    padding-left: 10px;">Welcome, </p>
    <p style="font-size: 1.5cm;
    margin-left: auto;
    margin-right: auto;">"{{ username }}"</p>
</div>
<div>
    <input type="file" ref="fileInput" style="display: none" @change="handleFileChange">
    <button class="takepic-button" @click="selectImage">Take</button>
</div>
<div v-if="image" class="imgBlock">
    <img :src="image" style="width:50%;height:50%" alt="Selected Image">
    <label class="txtPredict">Prediction: {{this.result_data}}</label>
</div>
</template>

<style>
.greeting{
    display: flex;
    flex-direction: row;
}
.takepic-button{
    display: block;
    width: 200px;
    margin: auto auto auto auto;
    height: 200px;
    border-radius: 50%;
    background-color: burlywood;
    font-size:1cm;
}
.takepic-button:hover{
    cursor: pointer;
    background-image: linear-gradient(#51A9EE, #147BCD);
    border-color: #1482D0;
    text-decoration: none;
}
.imgBlock{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.txtPredict{
    border: 3px solid black;
    margin-top: 10px;
    color: white;
    background-color: #48433c;
}
</style>