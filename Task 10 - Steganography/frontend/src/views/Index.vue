<template>
  <div id="index">

    <!-- Content -->
    <div class="content w3-padding">
      <div>
        <form @submit="stEncode" autocomplete="off">
          <p>
            Hide a message in the image (this one can take a few seconds) <br>
            When you type the source path type just the name of the file (instead of '/img/img1.png' type 'img1')
          </p>
          <label>
            <input v-model="stEncodedSource" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the source image name here " required
                   name="stDecSrc">
            <input v-model="stEncodedMessage" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the message here" required
                   name="stDecSrc">
          </label>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Hide the message!
          </button>
        </form>

        <p v-if="stEncodedResult">
          {{ stEncodedResult }}
          <br>
          <img src='../../../img/hidden.png'
               alt="Your encoded image"
               width="300" height="300">
        </p>
        <hr>
      </div>

      <div>
        <form @submit="stDecode" autocomplete="off">
          <p>
            Read hidden message from the image (this one can take a few more seconds) <br>
          </p>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Read the message!
          </button>
        </form>

        <p v-if="stDecodedResult"> Your hidden message: {{ stDecodedResult }} </p>
        <hr>
      </div>

      <h1> Bonus options: </h1>
      <hr>
      <div>
        <form @submit="cipher" autocomplete="off">
          <p> Cipher your text </p>
          <label>
            <input v-model="cipheredSourceText" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the plain text here" required
                   name="cipheredSourceText">
          </label>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Cipher
          </button>
        </form>
        <p v-if="cipheredText"> Your cipheredText: {{ cipheredText }} </p>
        <hr>
      </div>
      <div>
        <form @submit="decipher" autocomplete="off">
          <p> Decipher your text</p>
          <label>
            <input v-model="decipheredSourceText" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the ciphered text here" required
                   name="decipheredSourceText">
          </label>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Decipher
          </button>
        </form>

        <p v-if="decipheredText"> Your decipheredText: {{ decipheredText }} </p>
        <hr>
      </div>

    </div>
  </div>
</template>
<script>
import axios from 'axios'

const url = '/api/'

export default {
  name: 'Index',
  data() {
    return {
      stEncodedSource: '',
      stEncodedMessage: '',
      stEncodedResult: '',
      stDecodedResult: '',
      cipheredSourceText: '',
      cipheredText: '',
      decipheredSourceText: '',
      decipheredText: '',
    }
  },
  methods: {
    async stEncode(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}st/encode`, {
          "src": `${this.stEncodedSource}.png`,
          "message": this.stEncodedMessage,
          "dest": 'hidden.png'
        });
        this.stEncodedResult = res.data;
      } catch (err) {
        this.stEncodedResult = 'Something went wrong, please check if the server is running and the data is correct';
      }
    },
    async stDecode(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}st/decode`, {
          "src": 'hidden.png'
        });
        this.stDecodedResult = res.data;
      } catch (err) {
        this.stDecodedResult = 'Something went wrong, please check if the server is running and the data is correct';
      }
    },
    async cipher(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}cipher/encode`, {
          "text": this.cipheredSourceText,
        });
        this.cipheredText = res.data;
      } catch (err) {
        this.decipheredText = 'Something went wrong, please check if the server is running and the data is correct';
      }
    },
    async decipher(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}cipher/decode`, {
          "text": this.decipheredSourceText,
        });
        this.decipheredText = res.data;
      } catch (err) {
        this.decipheredText = 'Something went wrong, please check if the server is running and the data is correct';
      }
    },
  }
}
</script>
