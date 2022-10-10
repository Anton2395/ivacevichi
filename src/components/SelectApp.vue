<template>
    <div class="v-select">
        <div class="title" @click="ShowOption=!ShowOption">
            <p :class="{pick: statusPick}">{{PickOption.text}}</p>
            <img src="../assets/up-icon.svg" v-show="ShowOption">
            <img src="../assets/down-icon.svg" v-show="!ShowOption">
        </div>
        <div class="options" v-show="ShowOption">
            <p
                class="option"
                v-for="option in options"
                :key="option"
                @click="Pick(option)"
            >
                {{option.text}}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'placeholder',
        'options',
        'pick'
    ],
    created() {
        this.PickOption.text = this.placeholder
        if (this.pick) {
            this.statusPick = true
        }
    },
    data() {
        return{
            statusPick: false,
            PickOption: {
                text: 'Select'
            },
            ShowOption: false,
        }
    },
    methods: {
        Pick(option) {
            this.PickOption = option
            this.ShowOption = false
            this.statusPick =  true
            this.$emit('pickoption', this.PickOption)
        }
    },
    emits: [
        'pickoption'
    ],
    // watch: {
    //     // PickOption(newPick) {
    //     //     console.log('3', newPick)
    //     //     this.PickOption.text = newPick.text
    //     //     this.PickOption.value = newPick.value
            
    //     // }
    // }
}
</script>

<style scoped lang="scss">
    .pick {
        font-weight: 400;
        font-size: 18px;
        line-height: 131.5%;
        color: #262626;

    }
    .v-select {
        width: 100%;
        position: relative;
        font-family: 'Lato';
        font-style: normal;
    }

    .title {
        border: 1px solid #E1E2EB;
        height: 30px;
        border-radius: 9px;
        display: flex;
        font-weight: 400;
        font-size: 20px;
        line-height: 131.5%;
        color: #87869D;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
    }
    .options {
        position: absolute;
        top:  calc(100% + 10px);
        height: 310px;
        overflow: auto;
        width: 100%;
        background: #FCFCFC;
        border: 1px solid #E1E2EB;
        box-shadow: 0px 19px 24px rgba(160, 160, 160, 0.25);
        border-radius: 10px;
        padding: 10px;

        .option {
            padding: 10px;
            font-weight: 400;
            font-size: 16px;
            line-height: 131.5%;
            width: 100%;
            height: 41px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        .option:hover {
            background: #4F71C0;
            color: #FCFCFC;
        }
    }
    .options::-webkit-scrollbar {
        display: none;
    }

    /* Hide scrollbar for IE, Edge and Firefox */
    .options {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
    }
</style>