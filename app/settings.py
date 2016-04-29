from app import app, db, models
from flask import request, flash, redirect, url_for
from flask import session
from datetime import datetime


def default_settings(user_id, username):
    """
    Set default settings for a user
    :param user_id:
    :param username:
    """
    user = user_id
    display_name = username
    notification_time = datetime.now()
    notifications = False
    public = False
    settings = models.Settings(display_name, notification_time, notifications, public, user)
    db.session.add(settings)
    db.session.commit()
    print "default settings set"


@app.route('/save_general_settings', methods=['POST'])
def save_general_settings():
    user = session['user']
    the_user = models.User.query.filter_by(username=user).first()
    id = the_user.id
    settings = models.Settings.query.filter_by(user=id).first()
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


@app.route('/save_notification_settings', methods=['POST'])
def save_notification_settings():
    user = session['user']
    the_user = models.User.query.filter_by(username=user).first()
    id = the_user.id
    # settings = models.Settings.query.filter_by(user=id).first()
    # print settings

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
    # print models.Settings.query.filter_by(user=id).first()
    flash('User settings set', 'settings')
    return redirect(url_for('settings'))


@app.template_filter('getNameById')
def getNameById(id):
    """
    Filter to show the display name rather than the username
    :param id:  the id of the user
    :return:    the display name of the user
    """
    settings = models.Settings.query.filter_by(user=id).first()
    if settings is None:
        the_user = models.User.query.filter_by(id=id).first()
        print the_user
        if the_user is None:
            return "unknown"
        return the_user.username
    return settings.displayName


app.jinja_env.filters['getNameById'] = getNameById
