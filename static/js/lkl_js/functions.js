function getRadioValue(radioName) {
    var radios = document.getElementsByName(radioName);
    var value;
    for(var i = 0; i < radios.length; i++){
        if(radios[i].checked){
            value = radios[i].value;
            break;
        }
    }
    return value;
}
function setRadioStatus(radioName) {
    var radios = document.getElementsByName(radioName);
    for(var i = 0; i < radios.length; i++){
        if (radios[i].value === sessionStorage.getItem(radioName)){
            radios[i].checked = true;
            break;
        }
    }
}
function post(URL, PARAMS) {
    var temp = document.createElement('form');
    temp.action = URL;
    temp.method = "post";
    temp.style.display = "none";
    for (var x in PARAMS) {
        var obj = document.createElement("textarea");
        obj.name = x;
        obj.value = PARAMS[x];
        temp.appendChild(obj);
    }

    //获取csrf cookie并作为post数据递交达到{% csrf_token %}效果
    var csrftoken = getCookie('csrftoken');
    var csrf_token = document.createElement('input');
    csrf_token.name = 'csrfmiddlewaretoken';
    csrf_token.value = csrftoken;
    temp.appendChild(csrf_token);

    document.body.appendChild(temp);
    temp.submit();

    return false;
}

//来自：https://docs.djangoproject.com/en/2.1/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function corrected_id() {
    var uid = document.getElementById("uid");
    var reg = /2019\d{6}/;
    var error = document.getElementById("error");
    if (reg.exec(uid.value) === null){
        uid.style.borderBottom = "1px solid red";
        error.hidden = false;
        if (error.innerText.search(' 学号格式错误 ') === -1){
            var msg = document.createTextNode(' 学号格式错误 ');
            error.appendChild(msg);
        }
    } else if (reg.exec(uid.value)[0] === uid.value) {
        uid.style.borderBottom = null;
        error.hidden = true;
        error.innerText = null;
    }
}
function corrected_pwd() {
    var pwd = document.getElementById("pwd");
    console.log(pwd.value);
    var reg = /.{6}/;
    var error = document.getElementById("error");
    var is_match = reg.exec(pwd.value);
    if (is_match === null){
        pwd.style.borderBottom = "1px solid red";
        error.hidden = false;
        if (error.innerText.search(' 密码长度不得低于六位 ') === -1){
            var msg = document.createTextNode(' 密码长度不得低于六位 ');
            error.appendChild(msg);
        }
    } else if (is_match[0] === pwd.value) {
        pwd.style.borderBottom = null;
        error.hidden = true;
        error.innerText = null;
    }
}
function corrected_phone() {
    var phone = document.getElementById("phone");
    var reg = /^1((3[0-9])|(4[579])|(5[469])|(66)|(7[35678])|(8[0-9])|(9[89]))\d{8}$/;
    var error = document.getElementById("error");
    var is_match = reg.exec(phone.value);
    if (is_match === null){
        phone.style.borderBottom = "1px solid red";
        error.hidden = false;
        if (error.innerText.search(' 手机号格式错误 ') === -1){
            var msg = document.createTextNode(' 手机号格式错误 ');
            error.appendChild(msg);
        }
    } else if (is_match[0] === phone.value) {
        phone.style.borderBottom = null;
        error.hidden = true;
        error.innerText = null;
    }
}
function corrected_email() {
    var email = document.getElementById("email");
    var reg = /@./;
    var error = document.getElementById("error");
    var is_match = reg.exec(email.value);
    if (is_match === null){
        email.style.borderBottom = "1px solid red";
        error.hidden = false;
        if (error.innerText.search(' 邮箱格式错误 ') === -1){
            var msg = document.createTextNode(' 邮箱格式错误 ');
            error.appendChild(msg);
        }
    } else if (is_match[0] === email.value) {
        email.style.borderBottom = null;
        error.hidden = true;
        error.innerText = null;
    }
}
