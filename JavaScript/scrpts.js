$(document).ready(function (){


    $('#password-signup').on('input',function (){
        passwordValidation()
    })
    $('#retype-pass').on('input',function () {
        passwordValidation()
    })
    $('.comment1').append("comment1")

    function passwordValidation(){
        let password = $('#password-signup').val()
        let retypePassword = $('#retype-pass').val()
        if (password.length >= 6) {
            $('#Six-Character').text('Password is at least 6 characters').css("color","green")
        }
        else{
            $('#Six-Character').text('Password MUST be at 6 characters').css("color","red")
        }

        if(password === retypePassword){
            $('#matching-Password').text('Password match').css("color","green")
        }
        else{
            $('#matching-Password').text('Password DO NOT match').css("color","red")
        }
    }


})
