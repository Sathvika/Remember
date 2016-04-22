/**
 * Created by margiechubin on 4/13/16.
 */
<<<<<<< HEAD

function writePost() {
    var content = document.getElementById('writePost').value;
    console.log(content);
    var postMessage = document.getElementById('postMessage');
    postMessage.innerHTML = "";

    if (content !== "") {
        var contentData = JSON.stringify({content: content});
=======
function writePost() {
    var content = document.getElementById('writePost').value;
    console.log(content);

    if (content !== "") {
        console.log('has content yay');
        var contentData = JSON.stringify({content: content});
        console.log(contentData);
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec

        $.ajax({
            url: '/submitPost', //https://cs242project.herokuapp.com
            contentType: 'application/json',
            type: 'POST',
            data: contentData,
            dataType: 'json',
            success: function (dataReturned) {
                console.log(dataReturned);
<<<<<<< HEAD
                document.getElementById('writePost').value = "";
                postMessage.innerHTML = "New post created";
                $('#postMessage').removeClass('error').addClass('success');
            },
            error: function (err) {
                console.log(err);
                postMessage.innerHTML = "Error creating post";
                $('#postMessage').removeClass('success').addClass('error');
            }
        });
    } else {
        postMessage.innerHTML = "Please write something";
        $('#postMessage').removeClass('success').addClass('error');
    }
}
=======
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
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
