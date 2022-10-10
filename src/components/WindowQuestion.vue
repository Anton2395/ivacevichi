<template>
    <div class="model-overlay">
        <div class="window">
           <div class="button-back">
                <img @click="$emit('closewindow')" src="../assets/cross-icon.svg">
            </div>
            <div class="name-window">
                <p>{{nameWindow}}</p>
            </div>
            <div class="main-text">
                <p>{{text}}</p>
            </div>
            <slot></slot>
        </div>
    </div>
</template>

<script>

export default {
    emits: [
        'closewindow'
    ],
    props: [
        'nameWindow',
        'text'
    ]
}
</script>


<style lang="scss" scoped>
    .main-text {
        font-weight: 500;
        font-size: 20px;
        line-height: 150%;
        display: flex;
        align-items: center;
        text-align: center;
        color: #87869D;
        width: 100%;
        padding-left: 67px;
        padding-right: 67px;
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
            text-align: center;
            color: #262626;
        }
    }
    .button-back {
        display: flex;
        justify-content: flex-end;
        img {
            cursor: pointer;
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
</style>