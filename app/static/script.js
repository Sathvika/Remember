/**
 * Created by margiechubin on 4/13/16.
 */
function writePost() {
    var content = document.getElementById('writePost').value;
    console.log(content);

    if (content !== "") {
        console.log('has content yay');
        var contentData = JSON.stringify({content: content});
        console.log(contentData);

        $.ajax({
            url: '/submitPost', //https://cs242project.herokuapp.com
            contentType: 'application/json',
            type: 'POST',
            data: contentData,
            dataType: 'json',
            success: function (dataReturned) {
                console.log(dataReturned);
            },
            error: function (err) {
                console.log(err);
            }
        });
    } else {
        console.log("You may not submit blank content");
    }
}

function populatePosts() {
    //for now, use in console
    console.log('populating the posts');
    $.ajax({
        url: '/getPosts', //https://cs242project.herokuapp.com
        contentType: 'application/json',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data);
        },
        error: function (err) {
            console.log(err);
        }
    });
}

function changeSort() {
    var ascOrDesc = $('input[name="ascOrDesc"]:checked').val();
    console.log(ascOrDesc);
    if (ascOrDesc === 'Ascending'){

    } else {

    }
}

function createAccount() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('pass1').value;
    var password2 = document.getElementById('pass2').value;
    var formMsg = document.getElementById('formMsg');
    var formMsgSuccess = document.getElementById('formMsg-success');
    if (password !== password2) {
        console.log("passwords much match");
        formMsg.innerHTML = "Error: passwords much match";
    } else if (username === "") {
        console.log("Username is required");
        formMsg.innerHTML = "Error: Username is required";
    } else if (password === "") {
        console.log("Password is required");
        formMsg.innerHTML = "Error: Password is required";
    } else {
        formMsg.innerHTML = "";
        var user = JSON.stringify({username: username, password: password});
        $.ajax({
            url: '/createUser', //https://cs242project.herokuapp.com
            contentType: 'application/json',
            type: 'POST',
            data: user,
            dataType: 'json',
            success: function (dataReturned) {
                console.log(dataReturned);
                formMsgSuccess.innerHTML = "Success, user has been created"
            },
            error: function (err) {
                console.log(err);
            }
        });
    }
}

function getAllUsers() {
    $.ajax({
        url: '/getUsers', //https://cs242project.herokuapp.com
        contentType: 'application/json',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data);
        },
        error: function (err) {
            console.log(err);
        }
    });
}