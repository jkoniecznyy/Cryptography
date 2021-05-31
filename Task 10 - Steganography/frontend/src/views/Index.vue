<template>
  <div id="index">

    <!-- Content -->
    <div class="content w3-padding">
      <div>
        <form @submit="cipher" autocomplete="off">
          <p> Cipher your text before Steganography </p>
          <label>
            <input v-model="cipheredSourceText" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the text to be ciphered here" required
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

      <div>
        <form @submit="stEncode" autocomplete="off">
          <p> Hide a message in the image (this one can take a few seconds)</p>
          <label>
            <input v-model="stEncSrc" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the source image path here" required
                   name="stDecSrc">
            <input v-model="stEncMessage" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the message here" required
                   name="stDecSrc">
            <input v-model="stEncDestination" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the new image path here" required
                   name="stDecSrc">
          </label>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Hide the message!
          </button>
        </form>

        <p v-if="stEncResult"> {{ stEncResult }} </p>
        <hr>
      </div>

      <div>
        <form @submit="stDecode" autocomplete="off">
          <p> Read hidden message from the image (this one can take a few seconds)</p>
          <label>
            <input v-model="stDecSrc" class="w3-input w3-section w3-border" type="text"
                   placeholder="Please type the image path here" required
                   name="stDecSrc">
          </label>
          <button class="w3-button w3-black w3-section">
            <i class="fa fa-paper-plane"></i> Read the message!
          </button>
        </form>

        <p v-if="stDecResult"> Your hidden message: {{ stDecResult }} </p>
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
      cipheredSourceText: '',
      cipheredText: '',
      decipheredSourceText: '',
      decipheredText: '',
      stEncSrc: '',
      stEncMessage: '',
      stEncDestination: '',
      stEncResult: '',
      stDecSrc: '',
      stDecResult: '',
    }
  },
  methods: {
    async cipher(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}cipher/encode`, {
          "text": this.cipheredSourceText,
        });
        console.log(res.data)
        this.cipheredText = res.data;
      } catch (err) {
        console.log('Request failed')
        this.decipheredText = 'Something went wrong, please try again later';
      }
    },
    async decipher(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}cipher/decode`, {
          "text": this.decipheredSourceText,
        });
        console.log(res.data)
        this.decipheredText = res.data;
      } catch (err) {
        console.log('Request failed')
        this.decipheredText = 'Something went wrong, please try again later';
      }
    },
    async stEncode(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}st/encode`, {
          "src": `img/${this.stEncSrc}`,
          "message": this.stEncMessage,
          "dest": `img/${this.stEncDestination}`
        });
        console.log(res.data)
        this.stEncResult = res.data;
      } catch (err) {
        console.log('Request failed')
        this.stEncResult = 'Something went wrong, please try again later';
      }
    },
    async stDecode(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}st/decode`, {
          "text": `img/${this.stDecSrc}`,
        });
        console.log(res.data)
        this.stDecResult = res.data;
      } catch (err) {
        console.log('Request failed')
        this.stDecResult = 'Something went wrong, please try again later';
      }
    },
  }
}
</script>
