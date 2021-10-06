$(document).ready(function (){

    changeTextBoxColor();
    $('#password-signup').on('input',function (){
        passwordValidation()
    })
    $('#retype-pass').on('input',function () {
        passwordValidation()
    })
    searchQuery();
    $("input.textbox[type=text]").on('input',function (){
        changeTextBoxColor();
    })



})

function changeTextBoxColor(){
    if($("input.textbox[type=text]").val() === ''){
        $("input.textbox[type=text]").addClass("requiredBorder");
    }
    else{
        $("input.textbox[type=text]").removeClass("requiredBorder");
    }
}
    ///Query String
function searchQuery(){
    var queryURL = window.location.search;
    console.log(queryURL);
    var urlparameters = new URLSearchParams(queryURL);
    if(urlparameters.has('search-box')){
        var keyword = urlparameters.get('search-box');
        var upperCase = keyword.toUpperCase();
        switch(upperCase){
            case 'HELP':
            case 'HEPL'://common misspelling
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                break;
            case 'PALLET':
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                window.alert('pallet');
                break;
            case 'PRIVACY':
            case 'PRIVAY': //common misspelling
            case 'RIVACY': //common misspelling
            case 'PRIACY': //common misspelling
            case 'PRIVACY POLICY':
            case 'PRIVACY POLCY': //common misspelling
            case 'PRIVACY POLCIY':  //common misspelling
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                $('.Report-content').append("<p>1.  <a href='./PrivacyPolicy.html'>Privacy Policy</a></p>");
                break;
            case 'REPORT':
            case 'REPROT'://common misspelling
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                $('.Report-content').append("<p>1.  <a href='./add_Item'>New Safety Report</a></p>");
                $('.Report-content').append("<p>2.  <a href='./MySafetyReports.html'>My Reports</a></p>");
                $('.Report-content').append("<p>3.  <a href='./List.html'>All Reports</a></p>");
                break;
            case 'LAB':
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                $('.Report-content').append("<p>1.  <a href='./Item2.html'>Moisture Analyzer leaking Nitrogen</a></p>");
                $('.Report-content').append("<p>2.  <a href='./Item3.html'>Unlabelled Chemical</a></p>");
                break;
            default:
                $('#search-header').text('Sorry.... no results found for ' + "\""+keyword+"\"");
                $('#search-results').text('Suggestions:');
                $('#search-results').append("<p>&sdot; Try a different Keyword</p>")
                $('#search-results').append("<p>&sdot; Make sure keywords are spelled correctly</p>")
                $('#search-results').append("<p>&sdot; Try to make keywords more general</p>")
        }
    }

}


    ///Validates Password
    function passwordValidation(){
        let password = $("#password-signup").val();
        let retypePassword = $('#retype-pass').val();
        if (password.length >= 6) {
            $('#Six-Character').text('Password is at least 6 characters').css("color","green");
        }
        else{
            $('#Six-Character').text('Password MUST be at 6 characters').css("color","red");
        }
        //Test if password matches retype
        if(password === retypePassword){
            $('#matching-Password').text('Password match').css("color","green");
        }
        else {
            $('#matching-Password').text('Password DO NOT match').css("color","red");
        }
        ///contains upper case
        if(password.match(/[A-Z]/)){
            $('#contains-upper').text('Password contains at least 1 upper case character').css("color","green");
        }
        else{
            $('#contains-upper').text('Password DOES NOT contain at least 1 upper case').css("color","red");
        }

        if(password.match(/[a-z]/)){
            $('#contains-lower').text('Password contains at least 1 lower case character').css("color","green");
        }
        else{
            $('#contains-lower').text('Password DOES NOT contain at least 1 lower case').css("color","red");
        }
        ///Contains number
        if(password.match(/[0-9]/)){
            $('#contains-number').text('Password contains at least 1 number').css("color","green");
        }
        else{
            $('#contains-number').text('Password DOES NOT contain at least 1 number').css("color","red");
        }
    }