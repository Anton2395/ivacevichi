<template>
    <div class="model-overlay">
        <div class="window">
            <div class="button-back">
                <img @click="CloseWindow" src="../assets/cross-icon.svg">
            </div>
            <div class="name-window">
                <p>{{datawindow.nameWindow}}</p>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Название станка</p>
                    <input type="text" placeholder="Введите название станка" v-model="localParam.name">
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Модуль</p>
                    <input type="text" placeholder="Введите модуль станка" v-model="localParam.module">
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">IP адрес</p>
                    <input type="text" placeholder="Введите IP адрес" v-model="localParam.ip">
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Порт</p>
                    <input type="number" placeholder="Введите порт" v-model="localParam.port">
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Тип станка</p>
                    <select-app-vue
                        :placeholder="plaseholder"
                        :options="OptionsList"
                        :pick="pickType"
                        @pickoption="PickType"
                    />
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Место установки</p>
                    <input type="text" placeholder="Введите место установки станка" v-model="localParam.location">
                </div>
            </div>
            <div class="input-place">
                <div class="input-line">
                    <p class="name">Примечание</p>
                    <textarea placeholder="Введите примечание" v-model="localParam.note"></textarea>
                </div>
            </div>
            <div class="but-complite" @click="Complite">
                <button>
                    Сохранить
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import SelectAppVue from './SelectApp.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
    created() {
        this.localParam = Object.assign({}, this.datawindow.data)
        if (this.localParam.type_mash) {
            this.typeMash = this.datawindow.data.type_mash
            this.pickType = true
            this.plaseholder = this.localParam.type_mash.text
        } else {
            this.pickType = false
            this.plaseholder = "Введите тип станка"
        }
        this.addOptionsListType()
        
    },
    props: [
        'datawindow'
    ],
    computed: {
        ...mapGetters({
            ListStan: 'getListMashine',
            OptionsList: 'getOptionsList'
        })
    },
    methods: {
        ...mapActions({
            addOptionsListType: 'addOptionsListType',
            addNewMasine: 'addNewMasine',
            changeMashine: 'changeMashine'
        }),
        PickType(TypeMash) {
            console.log(TypeMash)
            this.localParam.typeMash = TypeMash
            this.typeMash = TypeMash
        },
        CloseWindow() {
            this.$emit('closewindow')
            this.localParam = {}
        },
        async Complite() {
            let data = {
                name: this.localParam.name,
                module: this.localParam.module,
                ip: this.localParam.ip,
                port: this.localParam.port,
                type_mashine_id: this.typeMash.id,
                location: this.localParam.location,
                note: this.localParam.note,
                status_id: 1,
                id: this.localParam.id,
            }
            if ( this.datawindow.nameWindow === 'Добавить новый станок' ) {
                this.addNewMasine(data)
            } else {
                this.changeMashine(data)
            }
            this.localParam = {}
            this.CloseWindow()
        }
    },
    components: {
        SelectAppVue,
    },
    emits: [
        'closewindow',
    ],
    data() {
        return {
            plaseholder: "",
            localParam: {},
            pickType: false,
            typeMash: {},
        }
    }
}
</script>

<style scoped lang="scss">
    .but-complite {
        
        width: 100%;
        display: flex;

        button {
            cursor: pointer;
            background: #4F71C0;
            width: 100%;
            border-radius: 9px;
            height: 50px;

            font-weight: 600;
            font-size: 24px;
            line-height: 131.5%;
            color: #F2F2F2;
            transition: all .2s;

            &:hover {
                background: #4f71c0e8;
            }

            &:active {
                background: #4f71c0d2;
            }
        }
    }
    .input-line {
        font-family: 'Lato';
        font-style: normal;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 15px;
        p{
            font-weight: 400;
            font-size: 15px;
            line-height: 131.5%;
            color: #87869D;
            margin-bottom: 10px;
        }
        textarea {
            border: 1px solid #E1E2EB;
            border-radius: 9px;
            width: 100%;
            padding: 20px;
            font-weight: 400;
            font-size: 20px;
            line-height: 131.5%;
        }
        input {
            border: 1px solid #E1E2EB;
            border-radius: 9px;
            width: 100%;
            height: 25px;
            padding: 20px;
            font-weight: 400;
            font-size: 20px;
            line-height: 131.5%;
        }
    }
    .model-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 98;
        background-color: #00000080;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .button-back {
        display: flex;
        justify-content: flex-end;
        img {
            cursor: pointer;
        }
    }
    .window {
        font-family: 'Lato';
        font-style: normal;
        width: 31%;
        background: #FCFCFC;
        border-radius: 10px;
        padding: 25px;
        display: flex;
        flex-direction: column;

    }
    .name-window {
        display: flex;
        justify-content: center;
        margin-top: 5px;
        margin-bottom: 4%;

        p {
            font-weight: 500;
            font-size: 24px;
            line-height: 29px;
            display: flex;
            align-items: center;
            color: #262626;
        }
    }
    input::placeholder {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 131.5%;
        color: #87869D;

    }
    textarea {
        font-family: 'Lato';
        font-style: normal;
    }
    textarea::placeholder {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 131.5%;
        color: #87869D;
    }
</style>
