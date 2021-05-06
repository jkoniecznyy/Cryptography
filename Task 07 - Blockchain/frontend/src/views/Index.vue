<template>
  <div id="index">
    <!-- Navbar (sit on top) -->
    <div class="w3-bar w3-white w3-wide w3-padding w3-top w3-card" >
      <img src="../assets/logo.png" class="w3-bar-item w3-button" id="logo" alt="Rick Astrley" width="100"
           height="100">
      <p class="w3-bar-item w3-button"><b>RAC</b>- Rick Astley Coin</p>
    </div>
    <br/>
    <br/>
    <br/>
    <br/>

    <!-- Content -->
    <div class="content w3-padding">

      <button @click="network" class="w3-button">
        Test if network works
        <img src="../assets/network.jpg" class="w3-bar-item w3-button" id="network" alt="network" width="80"
             height="50">
      </button>

      <h1 v-if="networkCheck"> The network is working properly
        <img src="../assets/network2.jpg" class="w3-bar-item w3-button" id="network2" alt="network2" width="80"
             height="50"></h1>
      <h1 v-if="!networkCheck"> The network is probably down 😔 </h1>

      <form @submit="onSubmit" autocomplete="off">
        <p> Create New Transaction </p>
        <input v-model="sender" class="w3-input w3-section w3-border" type="text" placeholder="Sender" required
               name="sender">
        <input v-model="recipient" class="w3-input w3-section w3-border" type="text" placeholder="Rick Astley"
               required name="recipient">
        <input v-model="amount" class="w3-input w3-section w3-border" type="text" placeholder="Amount(RAC)" required
               name="amount">
        <button class="w3-button w3-black w3-section">
          <i class="fa fa-paper-plane"></i> Create
        </button>
      </form>

      <button @click="mine" class="w3-button w3-section">
        Let's mine!
        <img src="../assets/mcpickaxe.png" class="w3-bar-item w3-button" id="pickaxe" alt="Pickaxe" width="80"
             height="50">
      </button>
      <br/>
      <pre v-if="mined" class="w3-card custombg">{{ JSON.stringify(minedData, null, '\t') }}</pre>


      <button @click="chain" class="w3-button w3-section">
        Get chain!
        <img src="../assets/chain.jpg" class="w3-bar-item w3-button" id="chain" alt="Chain" width="80"
             height="50">
      </button>
      <pre v-if="chained" class="w3-card custombg">{{ JSON.stringify(chainedData, null, 2) }}</pre>

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
      sender: '',
      recipient: '',
      amount: '',
      mined: false,
      minedData: '{"id":1,"name":"A green door","price":12.50,"tags":["home","green"]}',
      chained: false,
      chainedData: '',
      networkCheck: false,
    }
  },
  async mounted() {
  },
  async created() {
  },
  async updated() {
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault()
      try {
        let res = await axios.post(`${url}transactions/new`, {
          "sender": this.sender,
          "recipient": this.recipient,
          "amount": this.amount
        });
        console.log(res)
        return res.status === 200;
      } catch (err) {
        console.log('Request failed')
        return false
      }
    },
    mine: async function () {
      try {
        let res = await axios.get(`${url}mine`);
        console.log(res)
        this.mined = true
        this.minedData = res.data
      } catch (err) {
        console.log('Request failed')
        return false
      }
    },
    network: async function () {
      try {
        let res = await axios.get(`${url}networkstatus`);
        console.log(res)
        this.networkCheck = res.data === "The network is working properly";
      } catch (err) {
        console.log('Request failed')
        return false
      }
    },
    chain: async function () {
      try {
        let res = await axios.get(`${url}chain`);
        console.log(res)
        this.chained = true
        this.chainedData = res.data
      } catch (err) {
        console.log('Request failed')
        return false
      }
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>