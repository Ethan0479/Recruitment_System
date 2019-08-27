function appointment() {
    var appointment_one;
    var appointment_two;
    var appointment_three;

    if (document.getElementById("time_1_1").value !== '' && document.getElementById("time_2_1").value === ''){
        document.getElementById("time_2_1").value = '8:00-10:00';
    }
    if (document.getElementById("time_1_2").value !== '' && document.getElementById("time_2_2").value === ''){
        document.getElementById("time_2_2").value = '8:00-10:00';
    }
    if (document.getElementById("time_1_3").value !== '' && document.getElementById("time_2_3").value === ''){
        document.getElementById("time_2_3").value = '8:00-10:00';
    }

    if (document.getElementById("time_1_1").value === '' && document.getElementById("time_2_1").value === ''){
        appointment_one = '';
    } else{
        appointment_one = document.getElementById("time_1_1").value + "_" + document.getElementById("time_2_1").value;
    }

    if (document.getElementById("time_1_2").value === '' && document.getElementById("time_2_2").value === ''){
        appointment_two = '';
    } else{
        appointment_two = document.getElementById("time_1_2").value + "_" + document.getElementById("time_2_2").value;
    }

    if (document.getElementById("time_1_3").value === '' && document.getElementById("time_2_3").value === ''){
        appointment_three = '';
    } else{
        appointment_three = document.getElementById("time_1_3").value + "_" + document.getElementById("time_2_3").value;
    }

    var direction = document.getElementById("button_list").value;
    // console.log(direction);
    var csrf_token = getCookie('csrftoken');
    $.ajax({
        url: "/sign_up/",
        type: "POST",
        data: {'appointment_one': appointment_one,
                'appointment_two': appointment_two,
                'appointment_three': appointment_three,
                'direction': direction,
                'csrfmiddlewaretoken': csrf_token},
        success: function (result) {
            if (result === '200'){
                window.location.href = '/sign_up/'
            }
        }
    })
}
function is_choice() {
    var time_list = document.getElementsByName('direction');
    for (var i = 0; i < time_list.length; i++){
        if (time_list[i].value === ''){
            time_list[i].style.backgroundColor = "#ffffff";
            time_list[i].style.borderColor = "#d1d1d1";
            time_list[i].style.color = "#c1bfbf";
        }
    }
}