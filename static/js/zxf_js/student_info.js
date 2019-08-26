//修改评分按钮
function btnChange(btn, n) {
            var list = new Array("");
            for (j = 1; j <= n; j++) {
                list[j-1] = document.getElementById("btn" + j);
            }

            for (j = 1; j <= n; j++) {
                if (list[j-1].id === btn.id) {
                    btn.style.backgroundColor = "#2b7bff";
                    btn.style.color = "#ffffff";

                } else {
                    list[j-1].style.backgroundColor = "#ffffff";
                    list[j-1].style.color = "#2b7bff";
                }
            }
        }

//修改手机端宽度
function widthChangeTest1() {
    var t = setTimeout("var editor = document.getElementById(\"cke_id_content\");editor.style.width = \"300px\";editor.style.marginTop=\"20px\";editor.style.marginLeft=\"3%\"", 200);
}

//没用删掉
function widthChangeTest2() {
    var t = setTimeout("var editor = document.getElementById(\"cke_id_content\");editor.style.width = \"600px\";editor.style.marginTop=\"20px\";editor.style.marginLeft=\"3%\"", 200);
}

//该变宽度的同时不可编辑
function widthChangeTest4() {
    var t = setTimeout("var editor = document.getElementById(\"cke_id_content\");editor.style.width = \"740px\";editor.style.marginTop=\"20px\";editor.style.marginLeft=\"3%\";let fri = document.getElementsByClassName(\"cke_wysiwyg_frame cke_reset\");let body = fri[0].contentWindow.document.getElementsByClassName(\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\");let body0 = body[0];body0.contentEditable='false';", 200);
}

//修改编辑器的margin
function marginChangeTest2() {
    setTimeout("editor = document.getElementById(\"cke_id_content\");editor.style.marginLeft = \"8px\";editor.style.marginTop = \"20px\";", 200);
}

//问题框可编辑
function editQuestion(id) {
    let textarea = document.getElementById("question");
    let input = document.getElementById("sbt2");
    if (input.value === '保存'){
        var csrf_token = getCookie('csrftoken');
        var question = textarea.value;
        $.ajax({
            url:"/interview/management/"+id+"/",
            type:"POST",
            data:{
                'question':question,
                'csrfmiddlewaretoken': csrf_token,
            },
            success: function (result) {
                if (result === '200') {
                    textarea.value = question+'\n修改成功';
                }else {
                    textarea.value = question+'\n修改失败';
                }
            }
        });
        input.value = '修改问题';
        textarea.readOnly = true;
    } else {
        input.value = '保存';
        textarea.readOnly = false;
    }
}

//显示评论区
function changeFrom(score,evaluate) {
    var div = document.getElementById('markdiv');
    div.innerHTML = "<form action=\"test.html\" method=\"post\">\n" +
        "                <div id=\"mark\">\n" +
        "                    <label id=\"text_2\">评分:</label>\n" +
        "                    <input id=\"btn1\" type=\"button\" value=\"1\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn2\" type=\"button\" value=\"2\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn3\" type=\"button\" value=\"3\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn4\" type=\"button\" value=\"4\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn5\" type=\"button\" value=\"5\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn6\" type=\"button\" value=\"6\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn7\" type=\"button\" value=\"7\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn8\" type=\"button\" value=\"8\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn9\" type=\"button\" value=\"9\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                    <input id=\"btn10\" type=\"button\" value=\"10\" class=\"btn\" onclick=\"btnChange(this,10)\"/>\n" +
        "                </div>\n" +
        "                <br/>\n" +
        "                <div id=\"evaluate\">\n" +
        "                    <textarea id=\"evaluate_text\" style=\"width: 100%;height: 80px\">"+evaluate+"</textarea>\n" +
        "                    <br/>\n" +
        "                    <br/>\n" +
        "                    <input id=\"sbt3\" type=\"button\" class='sbt' value=\"提交\" onclick='submitEvaluate()'>\n" +
        "                </div>\n" +
        "            </form>"
    var btn = document.getElementById('btn'+score);
    btn.click();
    var div_ = document.getElementsByClassName('django-ckeditor-widget');
    var input = document.getElementById('sbt1');
    div_[0].removeChild(input);
}

//提交评论
function submitEvaluate() {
    var id = document.getElementById('stu_id').value;
    var scores = document.getElementById('mark').getElementsByTagName('INPUT');
    var a; //成绩
    for (i = 0; i < scores.length; i++) {
        var score = scores[i];
        if (score.style.backgroundColor === "rgb(43, 123, 255)") {
            a = score.value;
        }
    }
    var textarea = document.getElementById('evaluate_text');
    var evaluate = textarea.value;
    var csrf_token = getCookie('csrftoken');
    $.ajax({
            url:"/interview/management/"+id+"/",
            type:"POST",
            data:{
                'evaluate':evaluate,
                'csrfmiddlewaretoken': csrf_token,
                'scores':a,
            },
            success: function (result) {
                if (result === '200') {
                    textarea.value = evaluate+'\n提交成功';
                }else {
                    textarea.value = evaluate+'\n提交失败';
                }
            }
        });
}