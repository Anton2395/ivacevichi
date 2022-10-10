<template>
  <div class="all-window">
    <div class="left-panel" :class="{ little: widthLittle}">
      <div class="logo" :class="{ imgLittle: widthLittle}">
        <img alt="Login picture" class="image-item" src="../assets/logosmole.svg" @click="ToLoginPage">
      </div>
      <div class="route-but">
        <div class="top-button">
          <div v-show="accessButton" class="but-line" @click="changeBut(1)">
            <div class="el" :class="{ choice: choiceOne }"></div>
            <div class="icon-but" @click="changeBut(1)" :class="{ centerIcon: widthLittle }">
              <img v-show="!choiceOne" src="../assets/Setting-icon.svg">
              <img v-show="choiceOne" src="../assets/Setting-choice-icon.svg">
              <p :class="{ 'choice-color': choiceOne, hideText:  widthLittle}" >Оборудование</p>
            </div>
          </div>
          <div v-show="accessButton" class="but-line" @click="changeBut(2)">
            <div class="el" :class="{ choice: choiceTwo }"></div>
            <div class="icon-but"  :class="{ centerIcon: widthLittle }">
              <img v-show="!choiceTwo" src="../assets/Reports-icon.svg">
              <img v-show="choiceTwo" src="../assets/Reports-choice-icon.svg">
              <p :class="{ 'choice-color': choiceTwo, hideText:  widthLittle }">Отчёты</p>
            </div>
          </div>
          <div class="but-line" @click="changeBut(3)">
            <div class="el" :class="{ choice: choiceThrea }"></div>
            <div class="icon-but" @click="changeBut(3)" :class="{ centerIcon: widthLittle }">
              <img v-show="!choiceThrea" src="../assets/Dashboard-icon.svg">
              <img v-show="choiceThrea" src="../assets/Dashboard-choice-icon.svg">
              <transition name="fade">
                <p :class="{ 'choice-color': choiceThrea, hideText:  widthLittle }">Дашборд</p>
              </transition>
            </div>
          </div>
        </div>
        <div class="bottom-button">
          <div class="but-line" @click="openWindowShift()">
            <div class="el" :class="{ choice: choiceFour }"></div>
            <div class="icon-but" @click="openWindowShift()" :class="{ centerIcon: widthLittle }">
              <img v-show="!choiceFour" src="../assets/shift-icon.svg">
              <img v-show="choiceFour" src="../assets/shift-choice-icon.svg">
              <transition name="fade">
                <p :class="{ 'choice-color': choiceFour, hideText:  widthLittle }">Смены</p>
              </transition>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="other-pole" :class="{ littleOther: widthLittle}">
      <button @click="changeWidth" class="width-button">
        <img v-show="!widthLittle" src="../assets/arrow-left.svg">
        <img v-show="widthLittle" src="../assets/arrow-right.svg" >
      </button>
      <MashinList
        v-if="choiceOne"
      />
      <ReportList
        v-if="choiceTwo"
      />
      <DashboardList 
        v-if="choiceThrea"
      />
    </div>
    <transition name="fade" appear>
    <WindowQuestion
      @click.self="closeWindowShift"
      v-if="WindowParam.status"
      :nameWindow="WindowParam.name"
      :text="WindowParam.text"
      @closewindow="closeWindowShift"
      >
      <div class="input-line" v-for="item, index in listShift" :key="item">
        <div class="name-line-window">
          <p>Смена {{index+1}}</p>
        </div>
        <div class="form-line">
          <input type="time" v-model="item.start" :disabled="!accessButton">
          <input type="time" v-model="item.end" :disabled="!accessButton">
          <div @click="deleteShift(index)" class="image-window-line" v-show="accessButton">
            <img src="../assets/delete-icon.svg">
          </div>
        </div>
      </div>
      <div class="add-new-shift" v-show="accessButton">
        <button @click="addNewShift">+ Добавить смену</button>
      </div>
      <div class="save-shifts" v-show="accessButton">
        <button @click="SaveShiftDB">Сохранить</button>
      </div>
    </WindowQuestion>
    </transition>
    <WindowQuestion
      @click.self="goLogin"
      v-if="WindowNeedLogin"
      nameWindow="Авторизация"
      text="Необходимо авторизоваться"
      @closewindow="goLogin"
      >
      <div class="login-but-back">
        <button @click="goLogin">
          <p>OK</p>
        </button>
      </div>
    </WindowQuestion>
  </div>
</template>

<script>
import MashinList from '@/components/MashinList.vue'
import ReportList from '@/components/ReportList.vue'
import DashboardList from '@/components/DashboardList.vue';
import WindowQuestion from '@/components/WindowQuestion.vue';
import router from '@/router'
import { mapActions } from 'vuex'
import { mapGetters, mapMutations } from 'vuex'

export default {
  components: {
    MashinList,
    ReportList,
    DashboardList,
    WindowQuestion
},
  methods: {
    ...mapActions({
        getShift: 'getShifts',
        postNewShift: 'postNewShift'
    }),
    ...mapMutations({
      setLogOut: 'setLogOut',
      resetOpenWindow: 'resetOpenWindow'
    }),
    goLogin() {
      this.setLogOut()
      this.resetOpenWindow()
      router.push({ name: 'login'})
    },
    changeWidth() {
      this.widthLittle = !this.widthLittle
      // alert(this.widthLittle)
    },
    changeBut(num) {
      this.choiceOne = false;
      this.choiceTwo = false;
      this.choiceThrea = false;
      if (num===1) {
        this.choiceOne = true;
      } else if (num===2) {
        this.choiceTwo = true;
      } else if (num===3) {
        this.choiceThrea = true;
      }
    },
    async openWindowShift() {
      await this.getShift()
      this.choiceFour = true
      this.WindowParam.status = true
    },
    closeWindowShift() {
      this.choiceFour = false
      this.WindowParam.status = false
    },
    addNewShift() {
      this.listShift.push({
        id: this.listShift.length + 1,
        start: "",
        end: ""
      })
    },
    SaveShiftDB() {
      this.postNewShift(this.listShift)
      this.choiceFour = false
      this.WindowParam.status = false
    },
    deleteShift(index) {
      this.listShift.splice(index, 1)
    },
    ToLoginPage() {
      router.push({ name: 'login'})
      this.setLogOut()
    },
    checkAccess() {
      let answer = false
      if (this.roleUser == "dev") {
        answer = true
        this.WindowParam.name = "Добавление смен"
      } else {
        this.WindowParam.name = "Смены"
      }
      return answer
    }
  },
  watch: {
    roleUser() {
      this.accessButton = this.checkAccess()
    }
  },
  created() {
    this.accessButton = this.checkAccess()
  },
  computed: {
    ...mapGetters({
      listShift: "getListShift",
      roleUser: "getRoleUser",
      WindowNeedLogin: "getWindowNeedLogin"
    })
  },
  data() {
    return {
      choiceOne: false,
      choiceTwo: false,
      choiceThrea: true,
      choiceFour: false,
      widthLittle: false,
      WindowParam: {
        status: false,
        name: "Добавление смен",
        text: ""
      },
      accessButton: false,
      log: true
    }
  }
}
</script>

<style scoped lang="scss">
  .fade-enter-active, .fade-leave-active {
      transition: opacity .2s;
  }

  .fade-enter-from, .fade-leave-to {
      opacity: 0;
  }
  .login-but-back {
    margin-top: 25px;
    button {
      background: #4f71c000;
      border: 2px solid #4F71C0;
      border-radius: 9px;
      width: 50%;
      height: 54px;
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
  .add-new-shift {
    display: flex;
    padding-left: 35px;
    button {
      background: none;
      cursor: pointer;
      font-size: 20px;
      line-height: 131.5%;
      color: #4F71C0;
    }
  }
  .save-shifts {
    margin-top: 33px;

    button {
      background: #4F71C0;
      border-radius: 9px;
      height: 70px;
      width: 90%;
      font-weight: 600;
      font-size: 24px;
      line-height: 131.5%;
      color: #F2F2F2;
    }
  }
  .input-line {
    width: 100%;
    padding-bottom: 20px;

    .name-line-window {
      display: flex;
      font-size: 15px;
      line-height: 131.5%;
      color: #87869D;
      padding-left: 35px;
      padding-bottom: 10px;
    }

    .form-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-left: 35px;

      input {
        height: 54px;
        width: 225px;
        border: 1px solid #E1E2EB;
        border-radius: 9px;
        text-align: center;
        font-size: 20px;
        line-height: 131.5%;
        color: #87869D;
      }
      img {
        height: 21px;
        width: 19px;
      }
    }
  }
  .width-button {
    position: absolute;
    z-index: 1;
    background: 0;
    top: 50px;
    left: -16px;
  }
  .all-window {
    display: flex;
    height: 100%;
    width: 100%;
    align-items: stretch;
    justify-content: space-between;
    
    .left-panel {
      border: 1px solid #F2F4F9;
      box-shadow: 0px 4px 30px rgba(191, 191, 191, 0.25);
      border-radius: 6px;
      width: 15%;
      background: rgba(135, 134, 157, 0.01);
      overflow: hidden;
      transition: all .8s;
      z-index: 1;
      

      .logo {
        display: flex;
        height: 15%;
        transition: all .8s;
        align-items: center;
        justify-content: center;
        width: 50%;
        margin-left: auto;
        margin-right: auto;

        .image-item {
          cursor: pointer;
          width: 100%;
        }
      }

      .imgLittle {
        width: 70%;
      }
    }
    .little {
      width: 5%;
    }
    .other-pole {
      position: relative;
      width: 85%;
      background: #FCFCFC;
      transition: all .8s;
    }

    .littleOther {
      width: 95%;
    }

  }
  
  .route-but {
    display: flex;
    flex-direction: column;
    height: 85%;
    justify-content: space-between;

    .bottom-button {
      padding-bottom: 15%;
    }
  }
  .but-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3%;
    cursor: pointer;

    .icon-but {
      display: flex;
      width: 100%;
      margin-left: 30px;
      transition: all .2s;
      overflow: hidden;


      p {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 500;
        font-size: 20px;
        line-height: 24px;
        display: flex;
        transition: opacity 1s;
        align-items: center;
        color: #262626;
        margin-left: 5%;
      }
      .hideText {
        opacity: 0;
      }
      .choice-color {
        color: #4F71C0;
      }

      
    }

    .centerIcon {
      color: black;
    }

    .el {
      width: 0px;
      height: 50px;
      transition: all .2s;
    }
    .choice {
      width: 9px;
      background: #4F71C0;
      border-radius: 0px 4px 4px 0px;      
    }
  }

  
</style>