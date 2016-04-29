from app import app, db, models, photos
from flask import request, redirect, url_for, session
import string

@app.route('/upload', methods=['POST'])
def upload():
    """
    Upload a post
    Use Flask-Uploads for photo uploads
    :return: a redirect to write
    """
    form = request.form
    print request.files
    if request.method == 'POST' and 'photo' in request.files:
        pic = request.files['photo']
        filename = photos.save(pic)
        user = session['user']
        url = photos.url(filename)
        rec = models.Photo(filename=filename, user=user, url=url)
        db.session.add(rec)
        db.session.commit()
        if form is not None:
            res = add_post_to_db(form['content'], url)
            print res
        else:
            print "nothing to add to db"
    return redirect(url_for('write'))

def add_post_to_db(content, url):
    """
    Add a post to the database
    :param content:     the content field of the db model
    :param url:         the url field of the db model
    :return: OK
    """
    curr_user = session['user']
    the_user = models.User.query.filter_by(username=curr_user).first()
    id = the_user.id
    cont = models.Content(content=content, user=id, url=url)
    db.session.add(cont)
    db.session.commit()
    return "OK"

def update_post_in_db(id, content, url):
    post = models.Content.query.filter_by(id=id).first()

    models.Content.query.filter_by(id=id).update({"content": content, "url": url})
    db.session.commit()
    return "OK"


def get_word_freq_dict():
    freqs = {}
    posts = models.Content.query.all()
    for post in posts:
        content = post.content
        split = content.split(" ")
        for word in split:
            w = word.lower()
            w = w.encode('ascii', 'ignore')
            w = w.translate(string.maketrans("",""), string.punctuation)
            if len(w) > 2:
                if w in freqs:
                    freqs[w]['value'] += 1
                else:
                    freqs[w] = {'key':w,'value':1}
    return freqs

