import { createStore } from 'vuex'
import axios from 'axios'
// import router from '../router'
import { ElMessage } from 'element-plus'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
let cookie = document.cookie
cookie.split(' ').forEach(item => {
    if (item.includes('access_token')) {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + item.split('=')[1].slice(0, -1)
    }
})


function checkErrorLogin(data) {
  if (data.response.status == 403 && data.response.data.detail == "Invalid token or expired token.") {
    return true
  } else {
    return false
  }
}

let defaulListDashboard = [
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  },
  {
    name_mashine: "No connect",
    duration_work: null,
    duration_power: null,
    duration_bad: null,
    status_power: false,
    status_connect: {
      text: "Ожидание",
      color: "#F2994A"
    }
  }
]

export default createStore({
  state: {
    LoaderButtonLogin: false,
    LoginStatus: false,
    ListStan: [],
    OptionsList: [],
    ListData: [],
    ListDashboard: defaulListDashboard,
    listShift: [],
    userRole: "guest",
    windowNeedLogin: false
  },
  getters: {
    getLoginStatus(state) {
      return state.LoginStatus
    },
    getWindowNeedLogin(state) {
      return state.windowNeedLogin
    },
    getRoleUser(state) {
      return state.userRole
    },
    getLoaderButtonLogin(state) {
      return state.LoaderButtonLogin
    },
    getListMashine(state) {
      return state.ListStan
    },
    getOptionsList(state) {
      return state.OptionsList
    },
    getListData(state) {
      return state.ListData
    },
    getDataDashboard(state) {
      return state.ListDashboard
    },
    getListShift(state) {
      return state.listShift
    }
  },
  mutations: {
    setLoginLoaderChange(state) {
      state.LoaderButtonLogin = !state.LoaderButtonLogin
    },
    setLoginStatus(state, role) {
      state.LoginStatus = true
      state.userRole = role
    },
    setOpenWindow(store) {
      store.windowNeedLogin = true
    },
    resetOpenWindow(store) {
      store.windowNeedLogin = false
    },
    setRoleGuest(state) {
      state.userRole = "guest"
    },
    setMashList(state, data) {
      state.ListStan = data
    },
    setStatusToMashList(state, data) {
      data.forEach( el => {
        state.ListStan.forEach( (elMash, index) => {
          if (el.id == elMash.id) {
            state.ListStan[index].status = el.status
          }
        })
      })
    },
    setNewMashine(state, data) {
      state.ListStan.push(data)
    },
    setChangeMashine(state, data) {
      let index = state.ListStan.findIndex(function(item) {
        return item.id===data.id
      })
      state.ListStan[index] = data
    },
    setDeleteMashine(state, data) {
      let index = state.ListStan.findIndex(function(item) {
        return item.id===data
      })
      state.ListStan.splice(index, 1)
    },
    setOptionsList(state, data) {
      state.OptionsList = data
    },
    setListData(state, data) {
      state.ListData = data
    },
    setLogOut(state) {
      state.LoginStatus = false
    },
    setListDataDashboard(state, data) {
      state.ListDashboard = data
    },
    setDefaultDashboard(state) {
      state.ListDashboard = defaulListDashboard
    },
    setNewShifts(state, data) {
      state.listShift = data
    }
  },
  actions: {
    async Login(context, option) {
      context.commit('setLoginLoaderChange')
      await axios.post('login', option).then((response) => {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access_token
        // this.$cookies.set("access_token", response.data.access_token)
        axios.defaults.withCredentials = true;

        context.commit('setLoginStatus', response.data.role)
        // this.$router.push({ name: 'settings'})
      }).catch((error) => {
        console.log('error', error)
        if (error.response.status == 401 && error.response.data.detail == "Invalid credentials") {
          ElMessage({
            showClose: true,
            message: 'Неверный логин или пароль',
            type: 'error',
          })
        } else {
          ElMessage({
            showClose: true,
            message: 'Ошибка сервера',
            type: 'error',
          })
        }
        context.commit('setLogOut')
      })
      context.commit('setLoginLoaderChange')
    },
    async actMashineList(context) {
      let data = [] 
      await axios.get('mashine').then( response => {
        data = response.data
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
      context.commit('setMashList', data)
    },
    async actMashineListStatus(context) {
      let data = []
      await axios.get('mashine/status').then( response => {
        data = response.data
        context.commit('setStatusToMashList', data)
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
    },
    async addOptionsListType(context) {
      let data = []
      await axios.get('/mashine/type/').then( response => {
        data = response.data
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
      context.commit('setOptionsList', data)
    },
    async addNewMasine(context, option) {
      let data = {}
      await axios.post('mashine', option).then( response => {
        data = response.data
        console.log('add new mashine done')
      }).catch( error => {
        context.commit('setOpenWindow')
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          console.log(error)
        }
      })
      context.commit('setNewMashine', data)
    },
    async changeMashine(context, option) {
      let data = {}
      await axios.put('mashine/'+option.id, option).then( response => {
        data = response.data
        console.log('change mashine done')
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
      context.commit('setChangeMashine', data)
    },
    async deleteMashine(context, options) {
      await axios.delete('mashine/'+options).then( response => {
        if (response.data.status) {
          console.log('delete mashine done')
          context.commit('setDeleteMashine', options)
        }
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
    },
    async getParamMashine(context, options) {
      let data = []
      await axios.get('mashine/data/time/'+options.start+'/'+options.end).then( response => {
        data = response.data
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
      context.commit('setListData', data)
    },

    async getParamMachineNow(context) {
      let data = []
      await axios.get('mashine/param/now').then( response => {
        data = response.data
        context.commit('setListDataDashboard', data)
      }).catch( error => {
        console.log(error)
        alert('bad work request')
        context.commit('setDefaultDashboard')
      })
    },

    async getShifts(context) {
      await axios.get('mashine/shift/').then( response => {
        context.commit('setNewShifts', response.data)
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
    },

    async postNewShift(context, data) {
      await axios.post('mashine/shift/', data).then( response => {
        context.commit('setNewShifts', response.data)
      }).catch( error => {
        console.log(error)
        if (checkErrorLogin(error)) {
          context.commit('setLogOut')
          context.commit('setOpenWindow')
        }
      })
    }
    
  }
})
