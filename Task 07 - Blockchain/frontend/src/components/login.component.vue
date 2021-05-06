<template>
  <div class="w3-content w3-padding" id="LoginComponent">
    <div class="w3-container w3-padding-32" id="contact">
      <h2 class="w3-border-bottom w3-border-light-grey w3-padding-16"> <b id="login">Logowanie</b>  </h2>
      <form v-if="!isLogged" @submit="onSubmit" autocomplete="off">
        <input v-model="email" class="w3-input w3-section w3-border" type="text" placeholder="Email" required name="email">
        <input  v-model="password" class="w3-input w3-section w3-border" type="text" placeholder="Haslo" required name="password">
        <button @click="login" class="w3-button w3-black w3-section" >
          <i class="fa fa-paper-plane"></i> Zaloguj się
        </button>
      </form>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LoginComponent',
  data () {
    return {
      email: '',
      password: '',
      isLogged: false
    }
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault()
      await this.login(this.email, this.password)
    },
    async login(email, password) {
      let result = await UserService.login(email, password)
      if(result === true){
        this.isLogged = true
        await this.$router.push('/')
      }
    },
  }
}
</script>

