<template>
  <div class="main-plase">
    <div class="part-window">
      <div class="main-part">
        <div class="logo">
          <img alt="Login picture" src="../assets/logosmole.svg">
          <p>для Ивацевичдрев </p>
        </div>
        <div class="part-in-main">
          <div class="name">Вход</div>
          <div class="description"><p>Добро пожаловать! Пожалуйста, введите ваши данные</p></div>
          <div class="input-plase">
            <input type="text" placeholder="Введите логин" v-model="username" @keyup.enter="Login">
            <input type="password" placeholder="Введите пароль" v-model="password" @keyup.enter="Login">
          </div>
          <div class="button-plase">
            <div @click="Login">
              <button class="login-button">
                <p v-show="!Loader">Войти</p>
                <LoaderButton v-show="Loader" />
              </button>
            </div>
            <div class="text-other-button">
              <p>или</p>
            </div>
            <div>
              <button @click="toDashboard" class="dashboard-button">
                <p>Открыть дашборд</p>
              </button>
            </div>
          </div>
        </div>
      <div class="other"><p>MVLab 2022</p></div>
      </div>
    </div>
    <div class="part-pict">
      <!-- <img clss="pict-main" alt="Login picture" src="../assets/LoginPict.png"> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import router from 'router'
import LoaderButton from '@/components/LoaderButton.vue'
import { mapActions, mapMutations } from 'vuex'
import { mapGetters } from 'vuex'
// import { ElMessage } from 'element-plus'

export default {
  name: 'LoginPage',
  components: {
    LoaderButton,
  },
  computed: {
    ...mapGetters({
      Loader: 'getLoaderButtonLogin',
      StatusLogin: 'getLoginStatus'
    })
  },
  watch: {
    StatusLogin(val) {
      if (val) {
        this.$router.push({ name: 'settings'})
      }
    }
  },
  methods: {
    ...mapActions({
      test: 'Login'
    }),
    ...mapMutations({
      setRoleGuest: 'setRoleGuest'
    }),
    async Login() {
      
      this.Loader = true
      let data = {
        username: this.username,
        password: this.password
      }
      await this.test(data)
    },
    toDashboard() {
      this.setRoleGuest()
      this.$router.push({ name: 'settings'})
    }
  },
  data() {
    return {
      username: "",
      password: ""
    }
  }
}
</script>

<style scoped lang="scss">


.part-pict {
  width: 48%;
  height: 100%;
  background: url(../assets/LoginPict.png) no-repeat;
  background-size: cover;

  @media only screen and (max-width: 500px) {
    display: none;
  }
}

.part-window {
  display: flex;
  width: 52%;
  flex-direction: column;
  align-items: flex-start;

  .main-part {
    display: flex;
    height: 100%;
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
    
    .logo {
      display: flex;
      align-items: center;
      margin-left: 20%;
      width: 50%;
      height: 19%;

      p {
        width: 240px;

        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 150%;
        color: #87869D;
      }
    }
    .part-in-main {
      margin-left: 20%;
      height: 44%;
      width: 65%;
      display: flex;      
      flex-direction: column;
      align-items: flex-start;
      
      .name {
        margin-bottom: 3%;
        font-family: 'Lato';
        font-style: normal;
        font-weight: 600;
        font-size: 64px;
        line-height: 131.5%;
        color: #262626;
      }

      .description {
        margin-bottom: 6%;
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 150%;
        color: #87869D;

        p {
          text-align: left
        }
      }

      .input-plase {
        display: flex;
        flex-direction: column;
        width: 100%;

        input {
          margin-bottom: 3%;
          width: 74%;
          height: 65px;
          border: 1px solid #E1E2EB;
          border-radius: 9px;
          padding-left: 20px;
          font-family: 'Open Sans';
          font-style: normal;
          font-weight: 400;
          font-size: 20px;
          line-height: 131.5%;
        }
      }
      .button-plase {
        margin-top: 2%;
        width: 100%;

        div {
          margin-bottom: 3%;
        }

        .text-other-button {
          display: flex;
          padding-left: 34%;

          p {
            font-family: 'Lato';
            font-style: normal;
            font-weight: 400;
            font-size: 20px;
            line-height: 150%;
            color: #87869D;
          }
        }

        button {
          height: 76px;
          width: 74%;
          border-radius: 9px;
          display: flex;
          align-items: center;
          flex-direction: column;
          justify-content: center;
          transition: all .2s;
          p {
            font-family: 'Open Sans';
            font-style: normal;
            font-weight: 600;
            font-size: 24px;
            line-height: 131.5%;
            text-align: center;
            color: #FCFCFC;
          }
        }
        .login-button {
          background: #4F71C0;
          
          &:hover {
            background: #4f71c0ec;
          }

          &:active {
            background: #4f71c0ce;
          }
        }
        .dashboard-button {
          background: #4f71c000;
          border: 2px solid #4F71C0;
          border-radius: 9px;
          transition: all .2s;

          p {
            font-family: 'Lato';
            font-style: normal;
            font-weight: 600;
            font-size: 24px;
            line-height: 131.5%;
            color: #4F71C0;
          }

          &:hover {
            background: #4f71c023;
          }

          &:active {
            background: #4f71c04b;
          }
        }
      }
    }
  }

}

.other {
  height: 27%;
  padding-top: 26%;
  padding-left: 6%;
  display: flex;
  font-family: 'Lato';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 150%;
  color: #87869D;
}
.main-plase {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>