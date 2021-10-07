$(document).ready(function (){

    //calls the search function
    searchQuery();
    ///Calls the password Validation if the input password box gets data
    $('input.password').on('input',function () {
        passwordValidation();
    })
    ///Calls the password Validation if the input password box gets data
    $("input.textbox").on('input',function (){
        changeTextBoxColor();
    })
    ///Adds a new comment when box is submitted
    $('#submit-comment').on('click',function (){
        Comment();
    })


})
/*
    Adds a new comment to a previous report
 */
function Comment(){
    var newComment = $('#user-Comment').val();
    var UTCDate = new Date();
    var today= UTCDate.toDateString();
    $('#past-comments').append("<div class='comment1'><p class ='posted-comment'>"+ newComment + "</p><div><p class='posted-by'>Posted " + today + " by Stan Smith</p></div></div>");
}
/*
    changes a section to red if rules are not followed
 */
function changeTextBoxColor(){
    var fname = $('#first-name').val();
    //Makes sure there is at least on character in the first name box
    if(fname.match(/[a-zA-z]/)){
        $('#first-name').removeClass("requiredBorder");
    }
    else{
        $('#first-name').addClass("requiredBorder");
    }
    //Makes sure there is at least on character in the last name box
    var lname = $('#last-name').val();
    if(lname.match(/[a-zA-z]/)){
        $('#last-name').removeClass("requiredBorder");
    }
    else{
        $('#last-name').addClass("requiredBorder");
    }
    var emailText = $('#email-text').val();
    if(emailText.match(/[a-zA-z]/)){
        $("#email-text").removeClass("requiredBorder");
    }
    else{
        $("#email-text").addClass("requiredBorder");
    }
    //If password is blank flag an error
    if($("input.textbox[type=password]").val() === ''){
        $("input.textbox[type=password]").addClass("requiredBorder");
    }
    else{
        $("input.textbox[type=password]").removeClass("requiredBorder");
    }
    //If retype password space is blank flag an error
    if($("#retype-pass").val() === ''){
        $("#retype-pass").addClass("requiredBorder");
    }
    else{
        $("#retype-pass").removeClass("requiredBorder");
    }
}
    ///Query String
function searchQuery(){
    var queryURL = window.location.search;
    //console.log(queryURL);
    var urlparameters = new URLSearchParams(queryURL);
    if(urlparameters.has('search-box')){
        var keyword = urlparameters.get('search-box');
        var upperCase = keyword.toUpperCase();
        switch(upperCase){
            case 'HELP':
            case 'HEPL'://common misspelling
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                $('.Report-content').append("<p>1.  <a href='./Help.html'>Help</a></p>");
                break;
            case 'PALLET':
                $('#search-header').text('Search results found for the term ' + "\""+keyword+"\"");
                $('.Report-content').append("<p>1.  <a href='./Item.html'>Metal bracket protruding from pallet</a></p>");
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
        var password = $("#password-signup").val();
        var retypePassword = $('#retype-pass').val();
        /*
            Checks if password is at least 6 characters
            If so changes text green if not keeps it red
         */
        if (password.length >= 6) {
            $('#Six-Character').removeClass('warning');
            $('#Six-Character').text('Password is at least 6 characters').addClass('correct-format');
        }
        else{
            $('#Six-Character').removeClass('correct-format');
            $('#Six-Character').text('Password MUST be at 6 characters').addClass('warning');
        }
        /*Test if password matches retype
        If so changes text green if not keeps it red
         */
        if(password === retypePassword){
            $('#matching-Password').removeClass('warning');
            $('#matching-Password').text('Password match').addClass('correct-format');
        }
        else {
            $('#matching-Password').removeClass('correct-format');
            $('#matching-Password').text('Passwords DO NOT match').addClass('warning');
        }
        /*contains upper case
        If so changes text green if not keeps it red
         */
        if(password.match(/[A-Z]/)){
            $('#contains-upper').removeClass('warning');
            $('#contains-upper').text('Password contains at least 1 upper case character').addClass('correct-format');

        }
        else{
            $('#contains-upper').removeClass('correct-format');
            $('#contains-upper').text('Password DOES NOT contain at least 1 upper case').addClass('warning');
        }
        /*Test if password contains 1 lower case character
            If so changes text green
         */
        if(password.match(/[a-z]/)){
            $('#contains-lower').removeClass('warning');
            $('#contains-lower').text('Password contains at least 1 lower case character').addClass('correct-format');
        }
        else{
            $('#contains-lower').removeClass('correct-format');
            $('#contains-lower').text('Password DOES NOT contain at least 1 lower case').addClass('warning');
        }
        /*Checks if password Contains number
            If so changes text green if not keeps it red
         */
        if(password.match(/[0-9]/)){
            $('#contains-number').removeClass('warning');
            $('#contains-number').text('Password contains at least 1 number').addClass('correct-format');
        }
        else{
            $('#contains-number').removeClass('correct-format');
            $('#contains-number').text('Password DOES NOT contain at least 1 number').addClass('warning');
        }
    }