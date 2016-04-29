from app import app, models, posts, db, photos
from flask import request, render_template, redirect, url_for, session
from forms import SettingForm


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
    if the_user is None:
        session['user'] = None
        return redirect(url_for('index'))

    id = the_user.id
    the_settings = models.Settings.query.filter_by(user=id).first()
    display_name = the_settings.displayName

    return render_template('write.html', user=user, logged_in=logged_in, displayName=display_name)


@app.route('/read', methods=['GET'])
def read():
    user = session['user']
    logged_in = True
    the_user = models.User.query.filter_by(username=user).first()
    if the_user is None:
        session['user'] = None
        return redirect(url_for('index'))
    id = the_user.id
    the_settings = models.Settings.query.filter_by(user=id).first()
    display_name = the_settings.displayName
    public = the_settings.public
    whose_posts = "your"
    if public:
        posts = models.Content.query.all()
        whose_posts = "all"
    else:
        user = models.User.query.filter_by(username=user).first()
        id = the_user.id
        posts = models.Content.query.filter_by(user=id).all()
    return render_template('read.html', posts=posts, user=user, logged_in=logged_in, whose_posts=whose_posts,
                           displayName=display_name)


@app.route('/settings', methods=['GET'])
def settings():
    user = session['user']
    logged_in = True
    form = SettingForm()
    freq_data = posts.get_word_freq_dict()
    return render_template('settings.html', user=user, logged_in=logged_in, form=form, freq_data=freq_data)


@app.route('/edit', methods=['GET'])
def edit():
    user = session['user']
    logged_in = True
    the_user = models.User.query.filter_by(username=user).first()
    the_settings = models.Settings.query.filter_by(user=the_user.id).first()
    display_name = the_settings.displayName
    return render_template('editPost.html', user=user, logged_in=logged_in, displayName=display_name)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_by_id(id):
    user = session['user']
    logged_in = True
    the_user = models.User.query.filter_by(username=user).first()
    the_settings = models.Settings.query.filter_by(user=the_user.id).first()
    display_name = the_settings.displayName

    post = models.Content.query.filter_by(id=id).first()

    if request.method == 'POST' and 'photo' in request.files:
        form = request.form
        pic = request.files['photo']
        filename = photos.save(pic)
        user = session['user']
        url = photos.url(filename)
        rec = models.Photo(filename=filename, user=user, url=url)
        db.session.add(rec)
        db.session.commit()
        if form is not None:
            res = posts.update_post_in_db(id, form["content"], url)
            print res
        else:
            print "nothing to update in db"
        return redirect(url_for('read'))

    return render_template('editPost.html', post=post, user=user, logged_in=logged_in, displayName=display_name)