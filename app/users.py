from app import app, db, models, login_manager, settings
from flask import render_template, request, flash, redirect, url_for
from flask import session
from forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user):
    return models.User.query.get(user)


@login_manager.request_loader
def request_loader(request):
    users = models.User.query.all()
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
    return render_template('login.html', form=form)


def login_user(user):
    """
    Log the user in by setting the session cookie
    :param user: the user to log in
    """
    session['user'] = user
    flash('Logged in successfully.', 'login')


@app.route('/logout', methods=["GET"])
def logout():
    """
    Log the user out by setting the cookie user to none and redirecting to index
    :return: a redirect to index
    """
    print "logout"
    session['user'] = None
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register the user, log them in, then direct them to the writing page
    :return:    a redirect to write if registered successfully
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
        settings.default_settings(user.id, user.username)
        flash('User successfully registered', 'register')
        login_user(user.username)
        return redirect(url_for('write'))
    return render_template('register.html', form=form)
