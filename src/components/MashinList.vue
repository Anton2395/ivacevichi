<template>
    <div class="main-part">
        <transition name="fade" appear>
        <add-new-machine
            @click.self="ShowWindow=false"
            v-if="ShowWindow"
            @closewindow="closeWindow"
            :datawindow="DataWindow"
        />
        </transition>
        <transition name="fade" appear>
        <WindowQuestion
        @click.self="WindowParam.status = false"
        v-if="WindowParam.status"
        :nameWindow="WindowParam.name"
        :text="WindowParam.text"
        @closewindow="WindowParam.status = false"
        >
        <div class="but-delete-window" v-if="DeleteWindow">
            <button class="normal-but" @click="WindowParam.status = false">Отменить</button>
            <button class="red-but" @click="DeleteMashin(WindowParam.index)">Удалить</button>
        </div>
        <div class="but-delete-window" v-if="ErrorWindow">
          <button class="normal-but" @click="WindowParam.status = false">OK</button>
        </div>
        </WindowQuestion>
        </transition>
        <div class="header-place">
            <p class="name-space">Оборудование</p>
            <button class="add-but" @click="ClickAddNew"><p>+ Добавить станок</p></button>
        </div>
        <div class="body-place">
            <table class="main-param-table" cellspacing="0">
              <tr class="head-table">
                  <th class="name-colum">
                  <p>Название станка</p>
                  </th>
                  <th class="status-colum">
                  <p>Статус</p>
                  </th>
                  <th class="but-colum"></th>
              </tr>
              <!-- <TransitionGroup name="listt" class="container"> -->
                <tr class="line-data-table" v-for="item, index in ListStan" :key="item">
                  <td class="name-colum"><p>{{item.name}}</p></td>
                  <td class="status-colum"><p class="data-status" :style="{ background: item.status.color }">{{item.status.text}}</p></td>
                  <td class="but-colum">
                      <div @click="ClickChangeMashin(item, index)">
                      <img src="../assets/change-icon.svg">
                      </div>
                      <div @click="ClickDeleteMashin(index)">
                      <img src="../assets/delete-icon.svg">
                      </div>
                  </td>
                </tr>
              <!-- </TransitionGroup> -->
            </table>
        </div>
    </div>
</template>

<script>
import AddNewMachine from '@/components/AddNewMachine.vue';
import WindowQuestion from '@/components/WindowQuestion.vue';
import { mapActions, mapGetters } from 'vuex';

export default {
  components: {
    AddNewMachine,
    WindowQuestion,
  },
  computed: {
    ...mapGetters({
      ListStan: 'getListMashine',
    })
  },
  created() {
    this.actMashineList()
    this.startTimer()
  },
  unmounted() {
      this.stopTimer()
  },
  methods: {
    ...mapActions({
      actMashineList: 'actMashineList',
      actDeleteMashine: 'deleteMashine',
      getStatue: 'actMashineListStatus'
    }),
    ChangeMachin(Param, index) {
      this.ListStan[index]= Param
    },
    ClickAddNew() {
      this.DataWindow.nameWindow = 'Добавить новый станок',
      this.DataWindow.data = {}
      this.ShowWindow = true
    },
    ClickChangeMashin(data, index) {
      this.DataWindow.nameWindow = 'Редактировать станок',
      this.DataWindow.type_mash = data.type_mash
      this.DataWindow.data = data
      this.DataWindow.index = index
      this.ShowWindow = true
    },
    ClickDeleteMashin(index) {
      this.DeleteWindow = true
      this.WindowParam.status = true
      this.WindowParam.name = 'Удалить станок'
      this.WindowParam.text = 'Вы действительно хотите удалить станок? Данные не сохраняются.'
      this.WindowParam.index = index
    },
    DeleteMashin(index) {
      this.WindowParam.status = false
      this.actDeleteMashine(this.ListStan[index].id)
    },
    closeWindow() {
      this.ShowWindow=false
    },
    startTimer() {
        let getData = this.getStatue
        this.timer = setInterval(function() {
          getData()
        }, 3000)
    },
    stopTimer() {
        clearInterval(this.timer)
    }
  },
    data() {
    return {
      getData: null,
      DataWindow: {
        nameWindow: 'Добавить новый станок',
        data: {},
        index: null
      },
      WindowParam: {
        status: false,
        name: '',
        text: '',
        index: null
      },
      ErrorWindow: false,
      DeleteWindow: false,
      ShowWindow: false,
      choiceOne: true,
      choiceTwo: false,
      choiceThrea: false,
    };
  },
}
</script>


<style lang="scss" scoped>
    .but-delete-window {
        display: flex;
        justify-content: space-around;
        margin-top: 38px;
        font-family: 'Lato';
        font-style: normal;

        button {
            height: 54px;
            width: 237px;
            background: none;
            border-radius: 9px;
            cursor: pointer;
        }

        .normal-but {
            border: 2px solid #4F71C0;
            border-radius: 9px;
            font-weight: 600;
            font-size: 20px;
            line-height: 131.5%;
            color: #4F71C0;
            transition: all .2s;

            &:hover {
            background: #4f71c017;
            }
            &:active {
            background: #4f71c03d;
            }
        }
        .red-but {
            background: #EB5757;
            font-weight: 600;
            font-size: 20px;
            line-height: 131.5%;
            color: #F2F2F2;
            transition: all .2s;

            &:hover {
            background: #d44f4f;
            }
            &:active {
            background: #b94242;
            }
        }
    }

    .container {
    position: relative;
    padding: 0;
    }
    .listt-move, /* apply transition to moving elements */
    .listt-enter-active,
    .listt-leave-active {
    transition: all .4s ease;
    }

    .listt-enter-from,
    .listt-leave-to {
    opacity: 0;
    }
    .listt-leave-active {
    display: flex;
    position: absolute;
    width: 1534px;
    justify-content: flex-start;
    
    .name-colum {
        display: flex;
    }

    .status-colum {
        display: flex;
    }
    .but-colum {
        width: 444px;
    }
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .2s;
    }

    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
  
    .main-part {
        width: 100%;
        height: 100%;
    }
    .header-place {
    height: 10%;
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;

    .name-space {
      font-family: 'Lato';
      font-style: normal;
      font-weight: 500;
      font-size: 36px;
      line-height: 43px;
      display: flex;
      align-items: center;
      color: #262626;
    }
    
    button {
      cursor: pointer;
      height: 63px;
      width: 327px;
      background: #4F71C0;
      border-radius: 9px;
      display: flex;
      align-items: center;
      flex-direction: column;
      justify-content: center;
      transition: all .2s;

      &:hover {
            background: #4f71c0ec;
          }

      &:active {
        background: #4f71c0ce;
      }

      p {
        font-family: 'Open Sans';
        font-style: normal;
        font-weight: 600;
        font-size: 24px;
        line-height: 131.5%;
        color: #FCFCFC;
      }
    }
  }
  ::-webkit-scrollbar {
    width: 10px;
  }
  /* Track */
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
    background: #F2F4F9;
    border-radius: 6.5px; 
  }
  
  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #87869D;
    border-radius: 6.5px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #717083; 
  }
  .body-place {
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
    margin-top: 3%;
    height: 80%;
    overflow-y: auto;

    .main-param-table {
      font-family: 'Lato';
      font-style: normal;
      font-weight: 400;
      font-size: 22px;
      line-height: 26px;
      width: 100%;

      .line-data-table {
        .but-colum {
          display: flex;
          justify-content: flex-end;
          height: 77px;

          div {
            display: flex;
            align-items: center;
            margin-right: 9%;
          }
          div:last-child {
            margin-right: 16%;
          }
        }
        .data-status {
          border-radius: 8px;
          justify-content: center;
          font-family: 'Lato';
          font-style: normal;
          font-weight: 500;
          font-size: 20px;
          line-height: 24px;
          display: flex;
          align-items: center;
          text-align: center;
          color: #FCFCFC;
          // color: black;
        }

        &:nth-child(2n+1) {
          td {
            background: #f1f5fd;
            border: 1px solid #f1f5fd;
          }
          td:first-child {
            border-top-left-radius: 5px;
            border-bottom-left-radius: 5px;
          }

          td:last-child {
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
          }
        }

        
      }

      .head-table {
        
        th {
          background: #F2F2F2;
          border: 1px solid #F2F2F2;
        }

        th:first-child {
          border-top-left-radius: 5px;
          border-bottom-left-radius: 5px;
        }

        th:last-child {
          border-top-right-radius: 5px;
          border-bottom-right-radius: 5px;
        }
      }

      .name-colum {
        width: 44%;
      }

      .status-colum {
        width: 27%;

        
        p {
          display: flex;
          height: 43px;
          width: 161px;
        }
      }

      
      th {
        padding: 13px;
        padding-left: 25;
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 24px;
        color: #87869D;
        p {
          display: flex;
          align-items: center;
        }
      }

      td {
        padding: 15px;
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 22px;
        line-height: 26px;
        color: #262626;
        p {
          display: flex;
          align-items: center;
        }
      }
    }
  }
</style>