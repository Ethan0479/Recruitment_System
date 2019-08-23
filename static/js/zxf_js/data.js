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
    var time = document.getElementById('time');
    var divs = time.getElementsByTagName('div');
    var long = divs.length + 1;
    var div = document.createElement("DIV");
    var name = "date" + long;
    div.id = name + '_div';
    div.innerHTML = "日期:<input type=\"text\" name=\"" + name + "\"/><br/>\n" +
        "        <br/>\n" +
        "        时间:\n" +
        "        <input type=\"text\" name=\"" + name + "_1\"/>\n" +
        "        <input type=\"text\" name=\"" + name + "_2\"/>\n" +
        "        <input type=\"text\" name=\"" + name + "_3\"/>\n" +
        "        <input id=\"" + name + "\" type=\"button\" value=\"增加\" onclick=\"addTime(this)\"/>\n";
    var add = document.getElementById('add_date');
    time.insertBefore(div, add);
}

function postNum() {
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
            }
        }
    })
}