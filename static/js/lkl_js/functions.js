// function ToSecondPage() {
//     var name = document.getElementById('name').value;
//     var uid = document.getElementById('uid').value;
//     var pwd = document.getElementById('pwd').value;
//     var gender = getRadioValue('gender');
//     sessionStorage.setItem("name", name);
//     sessionStorage.setItem("uid", uid);
//     sessionStorage.setItem("pwd", pwd);
//     sessionStorage.setItem("gender", gender);
//     window.location.href = "../HTML/register2.html"
// }
// function ToThirdPage() {
//     var QQ = document.getElementById('QQ').value;
//     var phone = document.getElementById('phone').value;
//     var email = document.getElementById('email').value;
//     sessionStorage.setItem("QQ", QQ);
//     sessionStorage.setItem("phone", phone);
//     sessionStorage.setItem("email", email);
//     window.location.href = "../HTML/register3.html"
// }
// function ToForthPage() {
//     var college = document.getElementById('college').value;
//     var major = document.getElementById('major').value;
//     var newclass = document.getElementById('class').value;
//     sessionStorage.setItem("college", college);
//     sessionStorage.setItem("major", major);
//     sessionStorage.setItem("class", newclass);
//     window.location.href = "../HTML/register4.html"
// }
// function form_submit() {
//     var apartment = document.getElementById('apartment').value;
//     var dormitory = document.getElementById('dormitory').value;
// }
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