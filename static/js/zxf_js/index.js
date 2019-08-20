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
    if (btn.id === "btn1"){
        var btn_1 = document.getElementById("btn2");
        var btn_2 = document.getElementById("btn3");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
    }else if (btn.id === "btn2"){
        var btn_1 = document.getElementById("btn1");
        var btn_2 = document.getElementById("btn3");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
    }else if (btn.id === "btn3") {
        var btn_1 = document.getElementById("btn1");
        var btn_2 = document.getElementById("btn2");
        btn_1.style.backgroundColor = "#ffffff";
        btn_2.style.backgroundColor = "#ffffff";
        btn_1.style.color = "#bcbcbc";
        btn_2.style.color = "#bcbcbc";
    }else {
        alert("错误")
    }
}

//模拟鼠标点击按钮
function click(btnID){
    document.getElementById(btnID).click();
}
