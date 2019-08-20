//设置时间按钮
function timeSet(sel) {
    for (i = 0; i < sel.length; i++) {
        if (sel[i].selected === true) {
            sel.style.backgroundColor = '#ffffff';
            sel.style.color = "#bcbcbc";
            sel.style.border = "solid 1px #bcbcbc"
        } else {
            sel.style.backgroundColor = "#2b7bff";
            sel.style.color = "#ffffff";
            sel.style.border = "solid 1px #2b7bff"
        }
    }
}


// 修改开发设计秘书处按钮样式
function btnChange(btn) {
    btn.style.backgroundColor = "#2b7bff";
    btn.style.color = "#ffffff";
    var direction = document.getElementById("button_list");
    if (btn.id === "btn1"){
        var btn_1 = document.getElementById("btn2");
        var btn_2 = document.getElementById("btn3");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
        direction.value = "开发";
        var tip = document.getElementById("head_2").value;
        tip.innerHTML = "nishizhuma";
    }else if (btn.id === "btn2"){
        var btn_1 = document.getElementById("btn1");
        var btn_2 = document.getElementById("btn3");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
        direction.value = "设计";
    }else if (btn.id === "btn3") {
        var btn_1 = document.getElementById("btn1");
        var btn_2 = document.getElementById("btn2");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
        direction.value = "秘书处";
    }else {
        alert("错误")
    }
}

//模拟鼠标点击按钮
// function click(btnID){
//     document.getElementById(btnID).click();
// }
function btnClick(direction) {
    if (direction == '开发') {
        btnChange(document.getElementById('btn1'));
    } else if (direction == '设计') {
        btnChange(document.getElementById('btn2'));
    } else if (direction == '秘书处') {
        btnChange(document.getElementById('btn3'));
    } else {
        alert(direction);
    }
}

function selectClick(time1,time2,time3) {
    var time1_list = time1.split("_");
    var time2_list = time2.split("_");
    var time3_list = time3.split("_");
    var select_1_1 = document.getElementById('time_1_1').getElementsByClassName("opt");
    var select_2_1 = document.getElementById('time_2_1').getElementsByClassName("opt");
    var select_1_2 = document.getElementById('time_1_2').getElementsByClassName("opt");
    var select_2_2 = document.getElementById('time_2_2').getElementsByClassName("opt");
    var select_1_3 = document.getElementById('time_1_3').getElementsByClassName("opt");
    var select_2_3 = document.getElementById('time_2_3').getElementsByClassName("opt");
    for (i=0;i<select_1_1.length;i++){

    }
}