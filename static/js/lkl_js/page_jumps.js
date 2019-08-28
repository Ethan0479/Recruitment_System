//第一页
var firstpagehtml = '<form action="">\n' +
        '            <input type="text" id="name" placeholder="请输入姓名" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入姓名\'" name=""><br>\n' +
        '            <input type="number" id="uid" placeholder="请输入学号" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入学号\'" name="" onchange="corrected_id()"><br>\n' +
        '            <input type="password" id="pwd" placeholder="请输入密码" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入密码\'" name="" onchange="corrected_pwd()"><br>\n' +
        '            <span id="gender_tip" class="tip">请选择性别</span>&nbsp;\n' +
        '            <input type="radio" value="男" name="gender" hidden id="male" checked>\n' +
        '            <label class="male_icon" for="male"></label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n' +
        '            <input type="radio" id="female" value="女" name="gender" hidden>\n' +
        '            <label class="female_icon" for="female"></label>\n' +
        '            <br>\n' +
        '            <div class="main_footer">\n' +
        '                <input type="button" value="下&nbsp;&nbsp;一&nbsp;&nbsp;步" id="process" onclick="FirstToSecond()"><br>\n' +
        '                <img src="/static/img/第一页.svg" alt="" class="page">\n' +
        '            </div>\n' +
        '        </form>';
//第二页
var secondpagehtml = "<form action=\"\">\n" +
        "            <input type=\"number\" id=\"QQ\" placeholder=\"请输入QQ\" value='' onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入QQ'\" name=\"\"><br>\n" +
        "            <input type=\"number\" id=\"phone\" placeholder=\"请输入电话\" value='' onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入电话'\" name=\"\" onchange='corrected_phone()'><br>\n" +
        "            <input type=\"email\" id=\"email\" placeholder=\"请输入邮箱\" value='' onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入邮箱'\" name=\"\" onchange='corrected_email()'><br>\n" +
        "            <input type=\"text\" id=\"code\" placeholder=\"请输入验证码\" onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入验证码'\" name=\"\">\n" +
        "            <input type=\"button\" id=\"get_code\" value=\"邮箱验证码\" onclick='send_code()'>\n" +
        "            <br>\n" +
        "            <div class=\"main_footer\">\n" +
        "                <input type=\"button\" value=\"上&nbsp;&nbsp;一&nbsp;&nbsp;步\" id=\"process1\" onclick='SecondToFirst()'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n" +
        "                <input type=\"button\" value=\"下&nbsp;&nbsp;一&nbsp;&nbsp;步\" id=\"process\" onclick=\"SecondToThird()\"><br>\n" +
        "                <img src=\"/static/img/第二页.svg\" alt=\"\" class=\"page\">\n" +
        "            </div>\n" +
        "        </form>";
//第三页
var thirdpagehtml = '<form action="">\n' +
        '            <input type="text" id="class" placeholder="请输入班级" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入班级\'" name=""><br>\n' +
        '            <br>\n' +
        '            <div class="main_footer">\n' +
        '                <input type="button" value="上&nbsp;&nbsp;一&nbsp;&nbsp;步" id="process1" onclick="ThirdToSecond()">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n' +
        '                <input type="button" value="下&nbsp;&nbsp;一&nbsp;&nbsp;步" id="process" onclick="ThirdToForth()"><br>\n' +
        '                <img src="/static/img/第三页.svg" alt="" class="page">\n' +
        '            </div>\n' +
        '        </form>';
//第四页
var forthpagehtml = '<form action="">\n' +
    '            <div>\n' +
    '                <input type="number" id="dormitory" placeholder="请输入宿舍" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入宿舍\'" name="dormitory"><br>\n' +
    '            </div>\n' +
    '            <div class="main_footer">\n' +
    '                <input type="button" value="上&nbsp;&nbsp;一&nbsp;&nbsp;步" id="process1" onclick="ForthToThird()">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n' +
    '                <input type="button" value="提&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;交" id="process" onclick="Form_Submit()"><br>\n' +
    '                <img src="/static/img/第四页.svg" alt="" class="page">\n' +
    '            </div>\n' +
    '        </form>';
function FirstToSecond() {
    //保存当前页面数据
    var name = document.getElementById('name').value;
    var uid = document.getElementById('uid').value;
    var pwd = document.getElementById('pwd').value;
    var gender = getRadioValue('gender');
    sessionStorage.setItem("name", name);
    sessionStorage.setItem("uid", uid);
    sessionStorage.setItem("pwd", pwd);
    sessionStorage.setItem("gender", gender);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = secondpagehtml;
    //用于显示变化后的页面的值
    document.getElementById('QQ').value = sessionStorage.getItem('QQ');
    document.getElementById('phone').value = sessionStorage.getItem('phone');
    document.getElementById('email').value = sessionStorage.getItem('email');
    document.getElementById('code').value = sessionStorage.getItem('input_code');
}
function SecondToFirst() {
     //保存当前页面数据
    var QQ = document.getElementById('QQ').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var input_code = document.getElementById('code').value;
    sessionStorage.setItem("QQ", QQ);
    sessionStorage.setItem("phone", phone);
    sessionStorage.setItem("email", email);
    sessionStorage.setItem("input_code", input_code);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = firstpagehtml;
    //用于显示变化后的页面的值
    document.getElementById('name').value = sessionStorage.getItem('name');
    document.getElementById('uid').value = sessionStorage.getItem('uid');
    document.getElementById('pwd').value = sessionStorage.getItem('pwd');
    setRadioStatus('gender');
}
function SecondToThird() {
    //保存当前页面数据
    var QQ = document.getElementById('QQ').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var input_code = document.getElementById('code').value;
    sessionStorage.setItem("QQ", QQ);
    sessionStorage.setItem("phone", phone);
    sessionStorage.setItem("email", email);
    sessionStorage.setItem("input_code", input_code);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = thirdpagehtml;
    document.getElementById('college_list').hidden = false;
    document.getElementById('major_list').hidden = false;
    setTimeout("get_major();", 100);
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('college')){
        document.getElementById('college').value = sessionStorage.getItem('college');
    }
    if (sessionStorage.getItem('major')){
        setTimeout("document.getElementById('major').value = sessionStorage.getItem('major');", 100);
    }
    document.getElementById('class').value = sessionStorage.getItem('class');
}
function ThirdToSecond() {
     //保存当前页面数据
    var college = document.getElementById('college').value;
    var major = document.getElementById('major').value;
    sessionStorage.setItem("college", college);
    sessionStorage.setItem("major", major);
    sessionStorage.setItem("class", document.getElementById('class').value);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = secondpagehtml;
    document.getElementById('college_list').hidden = true;
    document.getElementById('major_list').hidden = true;
    //用于显示变化后的页面的值
    document.getElementById('QQ').value = sessionStorage.getItem('QQ');
    document.getElementById('phone').value = sessionStorage.getItem('phone');
    document.getElementById('email').value = sessionStorage.getItem('email');
    document.getElementById('code').value = sessionStorage.getItem('input_code');
}
function ThirdToForth() {
     //保存当前页面数据
    var college = document.getElementById('college').value;
    var major = document.getElementById('major').value;
    sessionStorage.setItem("college", college);
    sessionStorage.setItem("major", major);
    sessionStorage.setItem("class", document.getElementById('class').value);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = forthpagehtml;
    document.getElementById('college_list').hidden = true;
    document.getElementById('major_list').hidden = true;
    document.getElementById('apartment_list').hidden = false;
    document.getElementById('city_list').hidden = false;
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('city')){
        document.getElementById('city').value = sessionStorage.getItem('city');
    }
    if (sessionStorage.getItem('apartment')) {
        document.getElementById('apartment').value = sessionStorage.getItem('apartment');
    }
    document.getElementById('dormitory').value = sessionStorage.getItem('dormitory');
}
function ForthToThird() {
    //保存当前页面数据
    var city = document.getElementById('city').value;
    var apartment = document.getElementById('apartment').value;
    var dormitory = document.getElementById('dormitory').value;
    sessionStorage.setItem('city', city);
    sessionStorage.setItem("apartment", apartment);
    sessionStorage.setItem("dormitory", dormitory);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = thirdpagehtml;
    document.getElementById('college_list').hidden = false;
    document.getElementById('major_list').hidden = false;
    document.getElementById('apartment_list').hidden = true;
    document.getElementById('city_list').hidden = true;
    get_major();
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('college')){
        document.getElementById('college').value = sessionStorage.getItem('college');
    }
    if (sessionStorage.getItem('major')){
        setTimeout("document.getElementById('major').value = sessionStorage.getItem('major');", 100);
    }
    document.getElementById('class').value = sessionStorage.getItem('class');
}
function Form_Submit() {
    var city = document.getElementById('city').value;
    var apartment = document.getElementById('apartment').value;
    var dormitory = document.getElementById('dormitory').value;
    sessionStorage.setItem("city", city);
    sessionStorage.setItem("apartment", apartment);
    sessionStorage.setItem("dormitory", dormitory);
    if (sessionStorage.getItem('input_code') === sessionStorage.getItem('code')){
        var csrf_token = getCookie('csrftoken');
        $.ajax({
        url: '/register/',
        type: "POST",
        data:{'newname' : sessionStorage.getItem('name'),
        'newstudent_id' : sessionStorage.getItem('uid'),
        'password' : sessionStorage.getItem('pwd'),
        'gender' : sessionStorage.getItem('gender'),
        'college' : sessionStorage.getItem('college'),
        'major' : sessionStorage.getItem('major'),
        'newclass' : sessionStorage.getItem('class'),
        'phone' : sessionStorage.getItem('phone'),
        'qq' : sessionStorage.getItem('QQ'),
        'email' : sessionStorage.getItem('email'),
        'city' : sessionStorage.getItem('city'),
        'apartment' : sessionStorage.getItem('apartment'),
        'dormitory' : sessionStorage.getItem('dormitory'),
        'code' : sessionStorage.getItem('input_code'),
        'csrfmiddlewaretoken' : csrf_token},
        success:function (result) {
            if (result === '200'){
                swal({
                title : "注册成功",
                text : "快去登录报名吧(●'◡'●)ﾉ",
                type : "success",
                confirmButtonText : "确定",
                closeOnConfirm : false
            }, function () {
              window.location.href = '/login/'
            });} else {console.log(result);
            swal({
                title : "注册失败啦",
                //暂待修改
                text: '是不是学号已经注册过啦\n看看自己前面是不是有空忘记填',
                type : "error",
                confirmButtonText : "确定",
                closeOnConfirm : false
            }, function () {
              window.location.href = '/register/'
            });}
            }
    });
    } else {
        swal({
            title : "验证码输错了哦！",
            type : "error",
            confirmButtonText : "确定",
            closeOnConfirm : false
        }, function () {
            sessionStorage.removeItem('code');
            sessionStorage.removeItem('input_code');
            window.location.href = '/register/'
        });
    }
}
function send_code() {
    var email = document.getElementById('email').value;
    if (email === ''){
        document.getElementById('email').style.borderBottom = "1px solid red";
        var error = document.getElementById('error');
        error.hidden = false;
        var msg = document.createTextNode('没有邮箱怎么发哇！');
        error.appendChild(msg);
    }else{
        var code_button = document.getElementById('get_code');
        var wait_time = 60;
        $.ajax({
            url: "/email_code/",
            type: "POST",
            data: {'email': email,
                   'csrfmiddlewaretoken': getCookie('csrftoken')},
            success: function (result) {
                sessionStorage.setItem('code', result);
            }
        });
        count_down(wait_time, code_button);
        console.log('已发送！')
    }
}
function count_down(wait_time, button) {
        if (wait_time === 0){
            button.disabled = false;
            button.value = '邮箱验证码';
            button.style.backgroundColor = "#ffffff";
            wait_time = 60;
        } else {
            button.disabled = true;
            button.value = wait_time + 's';
            button.style.backgroundColor = '#eaeaea';
            wait_time--;
            setTimeout(function () {
                count_down(wait_time, button)
            }, 1000);
        }
    }
function get_major() {
    var academy;
    if (sessionStorage.getItem('college') === document.getElementById('college').value){
        academy = sessionStorage.getItem('college');
        console.log(sessionStorage.getItem('college'), document.getElementById('college').value);
    } else {
        academy = document.getElementById('college').value;
        console.log(sessionStorage.getItem('college'), document.getElementById('college').value);
    }
    var set_major = document.getElementById("major");
    var old_list = document.getElementById('major').getElementsByTagName('option');
    var length = old_list.length;
    for (var j = 1; j < length; j++){
        set_major.removeChild(old_list[1]);
    }
    set_major.value = '';
    $.ajax({
        url: "/get_major/",
        type: "POST",
        data: {'academy': academy,
                'csrfmiddlewaretoken': getCookie('csrftoken')},
        success: function (result) {
            if (result !== ''){
                var major_list = result.split(',');
                for (var i = 0; i < major_list.length; i++){
                    var item = document.createElement("option");
                    item.value = major_list[i];
                    var textnode = document.createTextNode(major_list[i]);
                    item.appendChild(textnode);
                    set_major.appendChild(item);
                }
            }else{
                var warn = document.createElement("option");
                warn.disabled = true;
                var warning_tip = document.createTextNode('本学院大一暂无专业！！！');
                warn.appendChild(warning_tip);
                set_major.appendChild(warn);
            }
        }
    });
}