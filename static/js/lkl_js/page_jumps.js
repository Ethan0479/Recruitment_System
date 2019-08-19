//第一页
var firstpagehtml = '<form action="">\n' +
        '            <input type="text" id="name" placeholder="请输入姓名" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入姓名\'" name=""><br>\n' +
        '            <input type="number" id="uid" placeholder="请输入学号" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入学号\'" name=""><br>\n' +
        '            <input type="password" id="pwd" placeholder="请输入密码" value="" onfocus="this.placeholder=\'\'" onblur="this.placeholder=\'请输入密码\'" name=""><br>\n' +
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
        "            <input type=\"number\" id=\"phone\" placeholder=\"请输入电话\" value='' onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入电话'\" name=\"\"><br>\n" +
        "            <input type=\"email\" id=\"email\" placeholder=\"请输入邮箱\" value='' onfocus=\"this.placeholder=''\" onblur=\"this.placeholder='请输入邮箱'\" name=\"\"><br>\n" +
        "            <br>\n" +
        "            <div class=\"main_footer\">\n" +
        "                <input type=\"button\" value=\"上&nbsp;&nbsp;一&nbsp;&nbsp;步\" id=\"process1\" onclick='SecondToFirst()'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n" +
        "                <input type=\"button\" value=\"下&nbsp;&nbsp;一&nbsp;&nbsp;步\" id=\"process\" onclick=\"SecondToThird()\"><br>\n" +
        "                <img src=\"/static/img/第二页.svg\" alt=\"\" class=\"page\">\n" +
        "            </div>\n" +
        "        </form>";
//第三页
var thirdpagehtml = '<form action="">\n' +
        '            <div class="selected">\n' +
        '                <!--<label class="tip">请选择学院</label>-->\n' +
        '                <label>\n' +
        '                    <select name="college" class="select_list" id="college">\n' +
        '                        <option value="学院1" selected="selected" class="tip" disabled>请选择学院</option>\n' +
        '                        <option value="学院2">学院1</option>\n' +
        '                        <option value="学院3">学院2</option>\n' +
        '                        <option value="学院4">学院3</option>\n' +
        '                    </select>\n' +
        '                </label>\n' +
        '            </div>\n' +
        '            <div class="selected">\n' +
        '                <!--<label class="tip">请选择专业</label>-->\n' +
        '                <label>\n' +
        '                    <select name="major" class="select_list" id="major">\n' +
        '                        <option value="专业1" selected="selected" class="tip" disabled>请选择专业</option>\n' +
        '                        <option value="专业2">专业1</option>\n' +
        '                        <option value="专业3">专业2</option>\n' +
        '                        <option value="专业4">专业3</option>\n' +
        '                    </select>\n' +
        '                </label>\n' +
        '            </div>\n' +
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
    '            <div class="selected">\n' +
    '                <!--<label class="tip">请选择学院</label>-->\n' +
    '                <label>\n' +
    '                    <select name="apartment" class="select_list" id="apartment">\n' +
    '                        <option value="" selected="selected" class="tip" disabled>请选择宿舍楼</option>\n' +
    '                        <option value="宿舍楼1">宿舍楼1</option>\n' +
    '                        <option value="宿舍楼2">宿舍楼2</option>\n' +
    '                        <option value="宿舍楼3">宿舍楼3</option>\n' +
    '                    </select>\n' +
    '                </label>\n' +
    '            </div>\n' +
    '            <div class="selected">\n' +
    '                <!--<label class="tip">请选择学院</label>-->\n' +
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
}
function SecondToFirst() {
     //保存当前页面数据
    var QQ = document.getElementById('QQ').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    sessionStorage.setItem("QQ", QQ);
    sessionStorage.setItem("phone", phone);
    sessionStorage.setItem("email", email);
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
    sessionStorage.setItem("QQ", QQ);
    sessionStorage.setItem("phone", phone);
    sessionStorage.setItem("email", email);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = thirdpagehtml;
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('college')){
        document.getElementById('college').value = sessionStorage.getItem('college');
    }
    if (sessionStorage.getItem('major')){
       document.getElementById('major').value = sessionStorage.getItem('major');
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
    //用于显示变化后的页面的值
    document.getElementById('QQ').value = sessionStorage.getItem('QQ');
    document.getElementById('phone').value = sessionStorage.getItem('phone');
    document.getElementById('email').value = sessionStorage.getItem('email');
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
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('apartment')) {
        document.getElementById('apartment').value = sessionStorage.getItem('apartment');
    }
    document.getElementById('dormitory').value = sessionStorage.getItem('dormitory');
}
function ForthToThird() {
    //保存当前页面数据
    var apartment = document.getElementById('apartment').value;
    var dormitory = document.getElementById('dormitory').value;
    sessionStorage.setItem("apartment", apartment);
    sessionStorage.setItem("dormitory", dormitory);
    //显示上/下一页面
    document.getElementById('submit').innerHTML = thirdpagehtml;
    //用于显示变化后的页面的值
    if (sessionStorage.getItem('college')){
        document.getElementById('college').value = sessionStorage.getItem('college');
    }
    if (sessionStorage.getItem('major')){
       document.getElementById('major').value = sessionStorage.getItem('major');
    }
    document.getElementById('class').value = sessionStorage.getItem('class');
}
function Form_Submit() {
    var apartment = document.getElementById('apartment').value;
    var dormitory = document.getElementById('dormitory').value;
    sessionStorage.setItem("apartment", apartment);
    sessionStorage.setItem("dormitory", dormitory);
    post('/register/', {
        'newname' : sessionStorage.getItem('name'),
        'newstudent_id' : sessionStorage.getItem('uid'),
        'password' : sessionStorage.getItem('pwd'),
        'gender' : sessionStorage.getItem('gender'),
        'college' : sessionStorage.getItem('college'),
        'major' : sessionStorage.getItem('major'),
        'newclass' : sessionStorage.getItem('class'),
        'phone' : sessionStorage.getItem('phone'),
        'qq' : sessionStorage.getItem('QQ'),
        'email' : sessionStorage.getItem('email'),
        'apartment' : sessionStorage.getItem('apartment'),
        'dormitory' : sessionStorage.getItem('dormitory')
    })
}