<template>
    <div class="main-part">
        <div class="header-place">
            <p class="name-space">Отчеты</p>
            <div class="forme-pole">
                <div class="date-range">
                    <el-date-picker
                        v-model="rangeDate"
                        type="daterange"
                        start-placeholder="Start date"
                        end-placeholder="End date"
                        format="DD/MM/YYYY"
                        popper-class="datePicker-my"
                    />
                </div>
                <button class="add-but" @click="downloadReportXML"><p>Скачать отчет</p></button>
            </div>
        </div>
        <div class="body-place" @wheel="scrolMouse">
            <div class="header-table">
                <div class="name-colum-head">
                    <div class="head-line">
                        <p>Название станка</p>
                    </div>
                </div>
                <div class="other-colum-place" id="test1">
                    <div class="colum">
                        <div class="head-main date-param">
                            <p>Дата</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main shift-param">
                            <p>Смена</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main good-time-param">
                            <p>Полезное время работы, ч</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main all-time-param">
                            <p>Общее время работы, ч</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main bad-time-param">
                            <p>Время простоя, ч</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main number-plates-param">
                            <p>Количество плит</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main number-part">
                            <p>Количество обработанных деталей</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main number-facings-param">
                            <p>Количество облицовок</p>
                        </div>
                    </div>
                    <div class="colum">
                        <div class="head-main conveyor-speed-param">
                            <p>Скорость транспортера, м/с</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="body-table" id="test3">
                <div class="name-colum paramm">
                    <div class="main-line" v-for="item in ListData" :key="item">
                        <p>{{item.name_mashine}}</p>
                    </div>
                </div>
                <div class="other-colum-place test" id="test2">
                    <div class="colum paramm">
                        <div class="main-line date-param" v-for="item in ListData" :key="item">
                            <p>{{item.date}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line shift-param" v-for="item in ListData" :key="item">
                            <p>{{item.shift}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line good-time-param" v-for="item in ListData" :key="item">
                            <p>{{item.duration_work}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line all-time-param" v-for="item in ListData" :key="item">
                            <p>{{item.duration_power}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line bad-time-param" v-for="item in ListData" :key="item">
                            <p>{{item.duration_bad}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line number-plates-param" v-for="item in ListData" :key="item">
                            <p>{{item.count_processed_boards}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line number-part" v-for="item in ListData" :key="item">
                            <p>{{item.count_processed_parts}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line number-facings-param" v-for="item in ListData" :key="item">
                            <p>{{item.count_facings}}</p>
                        </div>
                    </div>
                    <div class="colum paramm">
                        <div class="main-line conveyor-speed-param" v-for="item in ListData" :key="item">
                            <p>{{item.conveyor_speed}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- <div class="scrollbar-cont">
            <input type="range" min="0" :max="TestHeaght" v-model="testscroll" orient="vertical" class="slider">
        </div> -->
        <div class="scrollbar-cont">
            <input type="range" min="0" :max="TestHeaght" v-model="testscroll" orient="vertical" class="vertical slider">
            <input type="range" min="0" :max="maxWidthTable" v-model="valScroll" class="slider">
        </div>
    </div>
</template>

<script>
// import { HTTP } from '@/axios-conf.js';
import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'

export default {
    mounted() {
        let elem = document.getElementById('test1');
        this.maxWidthTable = elem.scrollWidth - elem.clientWidth
        let el = document.getElementsByClassName('paramm')[0]
        this.TestHeaght = el.scrollHeight - el.clientHeight
    },
    created() {
        this.actMashineList()
    },
    computed: {
        ...mapGetters({
            ListData: "getListData"
        })
    },
    methods: {
        ...mapActions({
            getData: 'getParamMashine',
            actMashineList: 'actMashineList'
        }),
        scrolMouse(event) {
            if (event.deltaY < 0 && this.testscroll >= 0) { 
                this.testscroll = this.testscroll + event.deltaY * 2
            }
            if (event.deltaY > 0 && this.testscroll < this.TestHeaght) {
                this.testscroll = this.testscroll + event.deltaY * 2
            }
        },
        async getParamBetween() {
            
            let date = {
                start: new Date(this.rangeDate[0]).getTime()/1000,
                end: new Date(this.rangeDate[1]).getTime()/1000
            }
            await this.getData(date)
            let el = document.getElementsByClassName('paramm')[0]
            this.TestHeaght = el.scrollHeight - el.clientHeight
        }, 

        downloadReportXML() {
            let textxml = '<?xml version="1.0"?><mashine-list>';

            this.ListData.forEach(element => {
                textxml = textxml + `
<mashine name='`+ element.name_mashine +`'>
    <name>`+ element.name_mashine +`</name>
    <date>`+ element.date + `</date>
    <shift>` + element.shift + `</shift>
    <duration_work>` + element.duration_work + `</duration_work>
    <duration_power>` + element.duration_power + `</duration_power>
    <duration_bad>` + element.duration_bad + `</duration_bad>
    <count_processed_parts>` + element.count_processed_parts + `</count_processed_parts>
    <count_facings>` + element.count_facings + `</count_facings>
    <count_processed_boards>` + element.count_processed_boards + `</count_processed_boards>
    <conveyor_speed>` + element.conveyor_speed + `</conveyor_speed>
</mashine>`
            });

            textxml = textxml + "</mashine-list>"

            let filename = "Report_"+ this.startDate + "_"+ this.endDate +".xml";
            let pom = document.createElement('a');
            let bb = new Blob([textxml], {type: 'text/plain'});

            pom.setAttribute('href', window.URL.createObjectURL(bb));
            pom.setAttribute('download', filename)

            pom.dataset.downloadurl = ['text/plain', pom.download, pom.href].join(':');
            pom.classList.add('dragout')

            pom.click();
        }
    },
    watch: {
        valScroll(newPix) {
            //////////
            let elem = document.getElementById('test1');
            this.maxWidthTable = elem.scrollWidth - elem.clientWidth
            //////////
            document.getElementById('test1').scrollTo(newPix, this.testscroll)
            document.getElementById('test2').scrollTo(newPix, this.testscroll)            
        },
        testscroll(newPix) {
            document.getElementById('test2').scrollTo(this.valScroll, newPix)
            for (let el of document.getElementsByClassName('paramm')) {
                el.scrollTo(this.valScroll, newPix)
                // console.log(el)
            }
        },
        rangeDate() {
            this.getParamBetween()
        }
    },
    data() {
        return{
            maxWidthTable: 1,
            TestHeaght: 1,
            valScroll: 0,
            testscroll: 0,
            startDate: "",
            endDate: "",
            rangeDate: ""
        }
    }
}
</script>

<style lang="scss" scoped>
    .header-table {
            width: 100%;
            height: 77px;
            display: flex;

            .name-colum-head {
                width: 35%;
                height: 77px;
                background: #FCFCFC;
                box-shadow: 9px 1px 5px rgba(186, 186, 186, 0.25);
                z-index: 1;

                .head-line {
                    display: flex;
                    width: 100%;
                    height: 77px;
                    background: #f2f2f270;
                    border-top-left-radius: 10px;
                    border-bottom-left-radius: 10px;

                    p {
                        margin: 25px;
                        font-weight: 400;
                        font-size: 20px;
                        line-height: 24px;
                        display: flex;
                        align-items: center;
                        color: #87869D;
                    }
                }
        
            }

            .date-param {
                p {
                    width: 116px;
                }
            }

            .shift-param {
                p {
                    width: 46px;
                }
            }

            .good-time-param {
                p {
                    width: 156px;
                }
            }

            .all-time-param {
                p {
                    width: 133px;
                }
            }

            .bad-time-param {
                p {
                    width: 102px;
                }
            }

            .number-plates-param {
                p {
                    width: 159px;
                }
            }

            .number-part {
                p {
                    width: 220px;
                }
            }

            .number-facings-param {
                p {
                    width: 123px;
                }
            }

            .conveyor-speed-param {
                p {
                    width: 193px;
                }
            }
    }

    .body-table {
        width: 100%;
        margin-right: 3%;
        display: flex;
        overflow: hidden;

        
    }
    

    .scrollbar-cont {
        width: 94%;
        margin-top: 18px;
        margin-left: 3%;
        margin-right: 3%;
        position: relative;

        
        .slider {
            -webkit-appearance: none;
            width: 100%;
            height: 10px;
            background: #F2F4F9;
            border-radius: 6.5px;
            outline: none;
            -webkit-transition: .2s;
            transition: opacity .2s;
        }
        
        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 63px;
            height: 10px;
            background: #87869D;
            border-radius: 6.5px;
        }
        .slider::-moz-range-thumb {
            width: 63px;
            height: 10px;
            background: #87869D;
            border-radius: 6.5px;
        }
        .vertical {
            position: absolute;
            right: -400px;
            bottom: 2140%;
            width: 750px;
            transform: rotate(-270deg);
        }
    }
    .colum:last-child {
        .main-line {
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        }
    }

    .other-colum-place {
        display: flex;
        width: 65%;
        justify-content: flex-start;
        overflow: hidden;

        .head-main {
            padding-left: 30px;
            display: flex;
            height: 77px;
            background: #f2f2f270;

            p {
                text-align: left;
                margin: 25px;
                margin-right: 0px;
                font-weight: 400;
                font-size: 20px;
                line-height: 24px;
                display: flex;
                align-items: center;
                color: #87869D;
            }
        }

        .main-line {
            padding-left: 30px;
            display: flex;
            height: 77px;

            p {
                margin: 25px;
                margin-right: 0px;
                font-weight: 400;
                font-size: 22px;
                line-height: 26px;
                display: flex;
                align-items: center;
                color: #262626;
            }

            &:nth-child(2n) {
                background: #f1f5fd;
                border: 1px solid #f1f5fd;
            }
        }

        .date-param {
                p {
                    width: 116px;
                }
            }

            .shift-param {
                p {
                    width: 46px;
                }
            }

        .good-time-param {
            p {
                width: 156px;
            }
        }

        .all-time-param {
            p {
                width: 133px;
            }
        }

        .bad-time-param {
            p {
                width: 102px;
            }
        }

        .number-plates-param {
            p {
                width: 159px;
            }
        }

        .number-part {
            p {
                width: 220px;
            }
        }

        .number-facings-param {
            p {
                width: 123px;
            }
        }

        .conveyor-speed-param {
            p {
                width: 193px;
            }
        }
    }


    .name-colum {
        width: 35%;
        height: 100%;
        background: #FCFCFC;
        box-shadow: 9px 1px 5px rgba(186, 186, 186, 0.25);
        overflow: hidden;
        z-index: 1;

        .main-line {
            &:nth-child(2n) {
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
        }
        .main-line {
            display: flex;
            width: 100%;
            height: 77px;
            
            p {
                margin: 25px;
                font-weight: 400;
                font-size: 22px;
                line-height: 26px;
                display: flex;
                align-items: center;
                color: #262626;
                flex: none;
                order: 0;
                flex-grow: 0;
            }

            &:nth-child(2n) {
                background: #f1f5fd;
                border: 1px solid #f1f5fd;
            }
        }

        .head-line {
            display: flex;
            width: 100%;
            height: 77px;
            background: #f2f2f270;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;

            p {
                margin: 25px;
                font-weight: 400;
                font-size: 20px;
                line-height: 24px;
                display: flex;
                align-items: center;
                color: #87869D;
            }
        }
    }
    
    .body-place {
        width: 94%;
        margin-left: 3%;
        margin-right: 3%;
        margin-top: 3%;
        height: 80%;
        display: flex;
        flex-direction: column;
    }
    .main-part {
        font-family: 'Lato';
        font-style: normal;
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
                font-family: 'Lato';
                font-style: normal;
                font-weight: 600;
                font-size: 24px;
                line-height: 131.5%;
                color: #FCFCFC;
            }
        }
    }

    .form-date {
        display: flex;
        align-items: center;
        border: 3px solid #4f71c088;
        border-radius: 6px;


        .input-form {
            margin: 4px;
            .line-form {
                display: flex;
                align-items: center;
                height: 27px;

                input {
                    height: 19px;
                }
            }
        }

        p {
            margin: 10px;
            font-family: 'Lato';
            font-style: normal;
            font-weight: 400;
            font-size: 20px;
            line-height: 131.5%;
        }

        button {
            width: 40px;
            border-radius: 6px;
        }
    }

    .forme-pole {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 700px;
    }
    
    .datePicker-my {
        font-family: 'Lato';
    }
</style>