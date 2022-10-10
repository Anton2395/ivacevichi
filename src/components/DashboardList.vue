<template>
    <div class="main-part">
        <div class="header-place">
            <p class="name-head">Дашборд</p>
        </div>
        <div class="body-place">
            <transition name="fade">
            <div class="window-param" id="window-hover" v-show="showWindow" :style="{ top:position.y+'px', left:position.x+'px'}">
                <div class="name-line">{{paramMashineShow.name}}</div>
                <div class="status-line" :style="{color:paramMashineShow.status.color}">{{paramMashineShow.status.text}}</div>
                <div class="line-param">
                    <div class="number-colum">{{paramMashineShow.good}} ч</div>
                    <div class="name-param-colum">Полезное время работы</div>
                </div>
                <div class="line-param">
                    <div class="number-colum">{{paramMashineShow.all}} ч</div>
                    <div class="name-param-colum">Общее время работы</div>
                </div>
                <div class="line-param">
                    <div class="number-colum">{{paramMashineShow.bad}} ч</div>
                    <div class="name-param-colum">Время простоя</div>
                </div>
            </div>
        </transition>
            <div class="pole-mashins" id="pole">
                <div class="colum">
                    <div class="name-colum">
                        <p>1 пролет</p>
                    </div>
                    <div class="first-line-fc">
                        <div class="seven-mashine mashine" :class="{powerPlace: getStatusPower(6)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(6)"
                        >
                            <p :class="{powerOn: getStatusPower(6), powerOff: !getStatusPower(6)}">7</p>
                        </div>
                        <div class="eght-mashine mashine" :class="{powerPlace: getStatusPower(7)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(7)"
                        >
                            <p :class="{powerOn: getStatusPower(7), powerOff: !getStatusPower(7)}">8</p>
                        </div>
                    </div>
                    <div class="second-line-fc">
                        <div class="four-mashine mashine" :class="{powerPlace: getStatusPower(3)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(3)"
                        >
                            <p :class="{powerOn: getStatusPower(3), powerOff: !getStatusPower(3)}">4</p>
                        </div>
                        <div class="five-mashine mashine" :class="{powerPlace: getStatusPower(4)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(4)"
                        >
                            <p :class="{powerOn: getStatusPower(4), powerOff: !getStatusPower(4)}">5</p>
                        </div>
                        <div class="six-mashine mashine" :class="{powerPlace: getStatusPower(5)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(5)"
                        >
                            <p :class="{powerOn: getStatusPower(5), powerOff: !getStatusPower(5)}">6</p>
                        </div>
                    </div>
                    <div class="therd-line-fc">
                        <div class="big-part">
                            <div class="two-mashine mashine" :class="{powerPlace: getStatusPower(1)}"
                                @mousemove.self="showParam" @mouseleave="clearWindowData"  @mouseover="inputDataToWindow(1)"
                            >
                                <p :class="{powerOn: getStatusPower(1), powerOff: !getStatusPower(1)}">2</p>
                            </div>
                            <div class="thre-mashine mashine" :class="{powerPlace: getStatusPower(2)}"
                                @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(2)"
                            >
                                <p :class="{powerOn: getStatusPower(2), powerOff: !getStatusPower(2)}">3</p>
                            </div>
                        </div>
                        <div class="smile-part">
                            <div class="one-mashine mashine" :class="{powerPlace: getStatusPower(0)}"
                                @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(0)"
                            >
                                <p :class="{powerOn: getStatusPower(0), powerOff: !getStatusPower(0)}">1</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="vl"></div>
                <div class="colum">
                    <div class="name-colum">
                        <p>2 пролет</p>
                    </div>
                    <div class="first-line-sc">
                        <div class="seventeen-mashine mashine" :class="{powerPlace: getStatusPower(15)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(15)"
                        >
                            <p :class="{powerOn: getStatusPower(15), powerOff: !getStatusPower(15)}">17</p>
                        </div>
                    </div>
                    <div class="second-line-sc"></div>
                    <div class="therd-line-sc">
                        <div class="ten-mashine mashine" :class="{powerPlace: getStatusPower(8)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(8)" 
                        >
                            <p :class="{powerOn: getStatusPower(8), powerOff: !getStatusPower(8)}">10</p>
                        </div>
                    </div>
                </div>
                <div class="vl"></div>
                <div class="colum">
                    <div class="name-colum">
                        <p>3 пролет</p>
                    </div>
                    <div class="first-line-tc">
                        <div class="eleven-mashine" :class="{powerPlace: getStatusPower(9)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(9)"
                        >
                            <p :class="{powerOn: getStatusPower(9), powerOff: !getStatusPower(9)}">11</p>
                        </div>
                        <div class="twelw-mashine" :class="{powerPlace: getStatusPower(10)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(10)"
                        >
                            <p :class="{powerOn: getStatusPower(10), powerOff: !getStatusPower(10)}">12</p>
                        </div>
                    </div>
                    <div class="second-line-tc">
                        <div class="therden-mashine" :class="{powerPlace: getStatusPower(11)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(11)"
                        >
                            <p :class="{powerOn: getStatusPower(11), powerOff: !getStatusPower(11)}">13</p>
                        </div>
                        <div class="forethen-mashine" :class="{powerPlace: getStatusPower(12)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(12)"
                        >
                            <p :class="{powerOn: getStatusPower(12), powerOff: !getStatusPower(12)}">14</p>
                        </div>
                    </div>
                    <div class="therd-line-tc">
                        <div class="fiveten-mashine" :class="{powerPlace: getStatusPower(13)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(13)"
                        >
                            <p :class="{powerOn: getStatusPower(13), powerOff: !getStatusPower(13)}">15</p>
                        </div>
                        <div class="sixten-mashine" :class="{powerPlace: getStatusPower(14)}"
                            @mousemove.self="showParam" @mouseleave="clearWindowData" @mouseover="inputDataToWindow(14)"
                        >
                            <p :class="{powerOn: getStatusPower(14), powerOff: !getStatusPower(14)}">16</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
    data() {
        return {
            statusPower: [
                {
                    status: false
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
                {
                    status: true
                },
            ],
            showWindow: false,
            position: {
                x:0,
                y:0,
            },
            paramMashineShow: {
                name: "asd",
                status: {
                    color: "#F2C94C",
                    text: "в ожидании"
                },
                good: 12,
                bad: 23,
                all: 246
            },
            timer: null
        }
    },
    computed: {
        ...mapGetters({
            DataDashboard: 'getDataDashboard',
        })
    },
    methods: {
        ...mapActions({
            getData: 'getParamMachineNow'
        }),
        getStatusPower(index) {
            return this.DataDashboard[index].status_power
        },
        inputDataToWindow(index) {
            this.paramMashineShow.name = this.DataDashboard[index].name_mashine
            this.paramMashineShow.status.color = this.DataDashboard[index].status_connect.color
            this.paramMashineShow.status.text = this.DataDashboard[index].status_connect.text
            this.paramMashineShow.good = this.DataDashboard[index].duration_work
            this.paramMashineShow.bad = this.DataDashboard[index].duration_bad
            this.paramMashineShow.all = this.DataDashboard[index].duration_power
        },
        clearWindowData() {
            this.showWindow = false
            // this.paramMashineShow.name = "No connect"
            // this.paramMashineShow.status.color = "#F2994A"
            // this.paramMashineShow.status.text = "Ожидание"
            // this.paramMashineShow.good = null
            // this.paramMashineShow.bad = null
            // this.paramMashineShow.all = null
        },
        showParam(event) {
            
            let pole = document.getElementById('pole').getBoundingClientRect()
            this.showWindow = true

            if (pole.left+pole.width > event.x+20+404) {
                this.position.x = event.layerX + 20
            } else {
                this.position.x = event.layerX - 404
            }
            if (pole.top+pole.height > event.y+25+179) {
                this.position.y = event.layerY + 25
            } else {
                this.position.y = event.layerY - 179 -25
            }
        },
        startTimer() {
            let getData = this.getData
            this.timer = setInterval(function() {
                getData()
            }, 3000)
        },
        stopTimer() {
            clearInterval(this.timer)
        }
    },
    created() {
        this.startTimer()
    },
    unmounted() {
        this.stopTimer()
    }
}
</script>

<style scoped lang="scss">
    .main-part {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 500;
        width: 100%;
        height: 100%;

        .header-place {
            display: flex;
            align-items: flex-end;
            height: 12%;
            padding-left: 41px;
            padding-bottom: 7px;
        }
        .body-place {
            height: 88%;
            padding-left: 41px;
            padding-top: 7px;
        }
    }

    .header-place {
        .name-head {
            font-family: 'Lato';
            font-size: 36px;
            line-height: 43px;
            display: flex;
            align-items: center;
            color: #262626;
        }
    }
    .body-place {
        position: relative;

        .pole-mashins {
            display: flex;
            align-items: center;
            height: 800px;
            width: 95%;
            background: #F2F4F9;
            border-radius: 20px;

            .vl {
                border-left: 1px solid #E1E2EB;
                height: 776px;
            }
            .colum {
                height: 100%;
                width: 33%;

                .name-colum {
                    display: flex;
                    align-items: flex-end;
                    justify-content: center;
                    height: 58px;

                    p {
                        font-size: 24px;
                        line-height: 29px;
                        color: #87869D;
                    }
                }
            }
        }
    }
    .first-line-fc {
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 100%;
        height: 230px;

        .seven-mashine {
            width: 171px;
            height: 73px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .eght-mashine {
            width: 171px;
            height: 73px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
    .second-line-fc {
        width: 100%;
        height: 230px;
        display: flex;
        align-items: center;
        justify-content: space-around;

        .four-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .five-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .six-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
    .therd-line-fc {
        width: 100%;
        height: 282px;

        .big-part {
            height: 60%;
            display: flex;
            align-items: center;
            justify-content: space-around;

            .two-mashine {
                width: 85px;
                height: 140px;
                border: 2px solid #4F71C0;
                border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .thre-mashine {
                width: 85px;
                height: 140px;
                border: 2px solid #4F71C0;
                border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
            }
        }

        .smile-part {
            height: 40%;
            display: flex;
            align-items: center;
            justify-content: center;

            .one-mashine {
                width: 171px;
                height: 73px;
                border: 2px solid #4F71C0;
                border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
            }
        }
    }

    .first-line-sc {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        height: 230px;
        padding-left: 10%;

        .seventeen-mashine {
            width: 171px;
            height: 73px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
    .second-line-sc {
        width: 100%;
        height: 230px;
        display: flex;
        align-items: center;
        justify-content: space-around;
    }
    .therd-line-sc {
        width: 100%;
        height: 169px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10%;

        .ten-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }

    .first-line-tc {
        width: 100%;
        height: 150px;
        display: flex;
        justify-content: flex-end;
        align-items: flex-start;
        padding-right: 3%;

        .eleven-mashine {
            margin-top: 5%;
            margin-right: 35%;
            width: 171px;
            height: 73px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .twelw-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
    
    .second-line-tc {
        width: 100%;
        height: 292px;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: space-between;
        padding-right: 3%;

        .therden-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .forethen-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }

    .therd-line-tc {
        width: 100%;
        height: 300px;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: space-evenly;
        padding-right: 3%;

        .fiveten-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .sixten-mashine {
            width: 85px;
            height: 140px;
            border: 2px solid #4F71C0;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
    .powerPlace {
        background: #4F71C0;
    }
    .powerOff {
        color: #4F71C0;
    }

    .powerOn {
        color: #FCFCFC;
    }

    .window-param {
        transition: top .1s, left .1s;
        position: absolute;
        width: 404px;
        height: 179px;
        background: #FCFCFC;
        box-shadow: 0px 11px 16px rgba(160, 160, 160, 0.25);
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: space-between;
        padding: 18px;


        .name-line {
            font-size: 20px;
            line-height: 131.5%;
            color: #262626;
        }
        .status-line {
            font-size: 14px;
            line-height: 131.5%;
        }
        .line-param {
            display: flex;
            justify-content: flex-start;
            font-size: 16px;
            line-height: 131.5%;
            color: #000000;

            .number-colum {
                width: 70px;
            }
        }
    }
    .fade-enter-active, .fade-leave-active {
        transition: opacity .2s;
    }

    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
</style>