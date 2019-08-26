function addTime(btn) {
    var divtime = document.getElementById(btn.id + '_div');
    var long = divtime.getElementsByTagName('INPUT');
    var input_text = document.createElement("INPUT");
    input_text.type = 'text';
    input_text.name = divtime.id + long;
    input_text.style.margin = '2px';
    divtime.insertBefore(input_text, btn)
}

function addDate(btn) {
    var time = document.getElementById('time_table');
    var divs = time.getElementsByTagName('div');
    var long = divs.length + 1;
    var div = document.createElement("DIV");
    var name = "date" + long;
    div.id = name + '_div';
    div.className = 'appoint_time';
    div.innerHTML = "日期:<input type=\"text\" class=\"date\"/><br/><br/>\n" +
        "时间:<input type=\"text\" class = \"text\"/><input type=\"text\" class = \"text\"/><input type=\"text\" class = \"text\"/><input id=\"" + name + "\" type=\"button\" value=\"增加\" onclick=\"addTime(this)\"/><br/>\n";
    var add = document.getElementById('add_date');
    time.insertBefore(div, add);
}

function getPostNum() {
    var b = document.getElementsByTagName('B');
    b[0].innerText = '生成中';
    var num = document.getElementById('num').value;
    var csrf_token = getCookie('csrftoken');
    $.ajax({
        url: "/data/manage/",
        type: "POST",
        data: {
            'num': num,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (result) {
            if (result === '200') {
                window.location.href = '/data/manage/'
            }else if(result === '数据生成出错，请输入数字'){
                b[0].innerText = result;
            }else if (result==='数据生成完成'){
                b[0].innerText = result;
            }
        }
    })
}

function getAppointmentTime() {
    var b = document.getElementsByTagName('B');
    b[1].innerText = '生成中';
    var appointment_time = document.getElementsByClassName("appoint_time");
    var long = appointment_time.length;
    var date = '';
    for (i = 1; i <= long; i++) {
        var timeList = $("#date"+i+"_div > input");
        for (j = 1; j < timeList.length-1; j++) {
            date = date + timeList[0].value + '_' + timeList[j].value + '@';
        }
        alert(date)
    }
    var csrf_token = getCookie('csrftoken');
    $.ajax({
        url: "/data/manage/timedata/",
        type: "POST",
        data: {
            'date': date,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (result) {
            if (result === '200') {
                window.location.href = '/data/manage/'
            }else if(result === '成功'){
                b[1].innerText = result;
            }else if (result==='错误'){
                b[1].innerText = result;
            }
        }
    })
}

function getAppointment(){
    var b = document.getElementsByTagName('B');
    b[2].innerText = '生成中';
    var appointment_time = document.getElementsByClassName("appoint_time");
    var long = appointment_time.length;
    var date = '';
    for (i = 1; i <= long; i++) {
        var timeList = $("#date"+i+"_div > input");
        for (j = 1; j < timeList.length-1; j++) {
            date = date + timeList[0].value + '_' + timeList[j].value + '@';
        }
    }
    var csrf_token = getCookie('csrftoken');
    $.ajax({
        url: "/data/manage/test/",
        type: "POST",
        data: {
            'date': date,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (result) {
            if (result === '200') {
                window.location.href = '/data/manage/'
            }else if(result === '成功'){
                b[2].innerText = result;
            }else if (result==='错误'){
                b[2].innerText = result;
            }
        }
    })
}