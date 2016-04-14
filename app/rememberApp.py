from app import app, db, models
from flask import render_template, request, jsonify


@app.route('/')
@app.route('/write', methods=['GET'])
def write():
    return render_template('write.html', text="Write a Post")


@app.route('/read', methods=['GET'])
def read():
    posts = models.Content.query.all()
    return render_template('read.html', text="View Posts", posts=posts)


@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html', text="SETTINGS")


@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html', text="Login or sign up")


@app.route('/submitPost', methods=['POST'])
def submitPost():
    form = request.json
    print form
    if form is not None:
        res = addPostToDB(form['content'])
        if res == "OK":
            return jsonify({'message': 'successful'})
    else:
        return jsonify({'message': 'failed'})


@app.route('/getPosts', methods=['GET'])
def getPosts():
    posts = models.Content.query.all()
    # print posts
    data = []
    for post in posts:
        data.append({'content': post.content, 'date': post.date, 'user': post.user})
    return jsonify({'message': 'OK', 'data': data})


@app.route('/createUser', methods=['POST'])
def createUser():
    # no duplicate users
    user = request.json
    #print user
    if user is not None:
        username = user["username"]
        password = user["password"]
        res = addUserToDB(username, password)
        if res == "OK":
            return jsonify({'message': 'successful'})
    return jsonify({'message': 'failed'})


@app.route('/getUsers', methods=['GET'])
def getUsers():
    users = models.User.query.all()
    data = []
    for user in users:
        data.append({'username': user.username})
    return jsonify({'users': data})


def addPostToDB(content):
    """
    Add a post to the database
    :param content:
    :return:
    """
    user = "me"
    cont = models.Content(content=content, user=user)
    db.session.add(cont)
    db.session.commit()
    return "OK"


def addUserToDB(username, password):
    """
    Add a user to the datebase
    :param username:
    :param password:
    :return:
    """
    newUser = models.User(username=username, password=password)
    db.session.add(newUser)
    db.session.commit()
    return "OK"
