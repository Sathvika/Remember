<<<<<<< HEAD
from app import app, db, models, login_manager
from flask import render_template, request, jsonify, flash, redirect, url_for
from flask import session
from forms import LoginForm, RegisterForm, SettingForm
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    user = session['user']
    logged_in = True
    if user is None:
        user = "not logged in"
        logged_in = False
    else:
        return redirect(url_for('write'))
    return render_template('notloggedin.html', user=user, logged_in=logged_in)


@app.route('/write', methods=['GET'])
def write():
    user = session['user']
    logged_in = True
    if user is None:
        return redirect(url_for('index'))

    the_user = models.User.query.filter_by(username=user).first()
    id = the_user.id
    settings = models.Settings.query.filter_by(user=id).first()
    displayName = settings.displayName
    print displayName
    return render_template('write.html', user=user, logged_in=logged_in, displayName=displayName)
=======
from app import app, db, models
from flask import render_template, request, jsonify


@app.route('/')
@app.route('/write', methods=['GET'])
def write():
    return render_template('write.html', text="Write a Post")
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec


@app.route('/read', methods=['GET'])
def read():
<<<<<<< HEAD
    user = session['user']
    logged_in = True
    the_user = models.User.query.filter_by(username=user).first()
    id = the_user.id
    settings = models.Settings.query.filter_by(user=id).first()
    displayName = settings.displayName
    public = settings.public
    whose_posts = "your"
    if public:
        posts = models.Content.query.all()
        whose_posts = "all"
    else:
        user = models.User.query.filter_by(username=user).first()
        id = the_user.id
        posts = models.Content.query.filter_by(user=id).all()
    return render_template('read.html', posts=posts, user=user, logged_in=logged_in, whose_posts=whose_posts,
                           displayName=displayName)

@app.route('/settings', methods=['GET'])
def settings():
    user = session['user']
    logged_in = True
    form = SettingForm()
    return render_template('settings.html', user=user, logged_in=logged_in, form=form)
=======
    posts = models.Content.query.all()
    return render_template('read.html', text="View Posts", posts=posts)


@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html', text="SETTINGS")


@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html', text="Login or sign up")
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec


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


<<<<<<< HEAD
@login_manager.user_loader
def load_user(user):
    return models.User.query.get(user)


@login_manager.request_loader
def request_loader(request):
    users = models.User.query.all()
    print users
    username = request.form.get('username')
    password = request.form.get('password')
    if username not in users:
        return
    user = models.User(username=username, password=password)
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', text="Login or sign up", form=form)
    user = request.form.get('username')
    password = request.form.get('password')
    if user != "" and password != "":
        login_user(user)
        return redirect(url_for('write'))

    '''
    if form.validate_on_submit():
        print "hello"
        # Login and validate the user.
        user = request.form.get('username')
        password = request.form.get('password')
        # need to validate password
        login_user(user)

        return redirect(url_for('write'))
    '''
    return render_template('login.html', form=form)


def login_user(user):
    """
    Log the user in by setting the session cookie
    :param user: the user to log in
    """
    session['user'] = user
    print session['user']
    flash('Logged in successfully.', 'login')


@app.route('/logout', methods=["GET"])
def logout():
    """
    Log the user out by setting the cookie user to none and redirecting to index
    :return: a redirect
    """
    print "logout"
    session['user'] = None
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register the user, log them in, then direct them to the writing page
    :return:
    """
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    user = request.form['username']
    password = request.form['password']
    if user != "" and password != "":
        user = models.User(user, password)
        db.session.add(user)
        db.session.commit()
        defaultSettings(user.id, user.username)
        flash('User successfully registered', 'register')
        login_user(user.username)
        return redirect(url_for('write'))
    '''
    if form.validate_on_submit():
        user = models.User(request.form['username'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        defaultSettings(user.id, user.username)
        flash('User successfully registered', 'register')
        login_user(user.username)
        return redirect(url_for('write'))
    '''
    return render_template('register.html', form=form)


def defaultSettings(user_id, username):
    user = user_id
    displayName = username
    notificationTime = datetime.now()
    notifications = False
    public = False
    settings = models.Settings(displayName, notificationTime, notifications, public, user)
    db.session.add(settings)
    db.session.commit()
    print "default settings set"
=======
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
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec


def addPostToDB(content):
    """
    Add a post to the database
    :param content:
<<<<<<< HEAD
    :return: OK
    """
    curr_user = session['user']
    the_user = models.User.query.filter_by(username=curr_user).first()
    print the_user
    id = the_user.id
    cont = models.Content(content=content, user=id)
=======
    :return:
    """
    user = "me"
    cont = models.Content(content=content, user=user)
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
    db.session.add(cont)
    db.session.commit()
    return "OK"


<<<<<<< HEAD
@app.route('/saveGeneralSettings', methods=['POST'])
def saveGeneralSettings():
    user = session['user']
    the_user = models.User.query.filter_by(username=user).first()
    # print the_user
    id = the_user.id
    settings = models.Settings.query.filter_by(user=id).first()
    # print settings
    display_name = request.form.get('displayName')
    if display_name is None or display_name == "":
        display_name = settings.displayName

    public = request.form.get('public')
    if public == 'y':
        public = True
    else:
        public = False

    models.Settings.query.filter_by(user=id).update({"displayName": display_name, "public": public})
    db.session.commit()
    print models.Settings.query.filter_by(user=id).first()
    flash('User settings set', 'settings')
    return redirect(url_for('settings'))


@app.route('/saveNotificationSettings', methods=['POST'])
def saveNotificationSettings():
    user = session['user']
    the_user = models.User.query.filter_by(username=user).first()
    # print the_user
    id = the_user.id
    # settings = models.Settings.query.filter_by(user=id).first()
    print settings

    time = request.form.get('notificationTime')
    if time is None:
        time = settings.notificationTime

    notifications = request.form.get('notifications')
    if notifications == 'y':
        notifications = True
    else:
        notifications = False

    models.Settings.query.filter_by(user=id).update({"notificationTime": time, "notifications": notifications})
    db.session.commit()
    print models.Settings.query.filter_by(user=id).first()
    flash('User settings set', 'settings')
    return redirect(url_for('settings'))

@app.template_filter('getNameById')
def getNameById(id):
    settings = models.Settings.query.filter_by(user=id).first()
    if settings is None:
        the_user = models.User.query.filter_by(id=id).first()
        print the_user
        if the_user is None:
            return "unknown"
        return the_user.username
    return settings.displayName
app.jinja_env.filters['getNameById'] = getNameById
=======
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
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
