from wtforms import Form, StringField, PasswordField, DateTimeField, BooleanField
from wtforms.validators import InputRequired, EqualTo


class LoginForm(Form):
    username = StringField('Username', [InputRequired("please enter your username")])
    password = PasswordField('Password', [InputRequired("please enter your password")])

    # remember = BooleanField('Remember me', default=False)

    def validate_on_submit(self):
        print "hello there"
        if not Form.validate(self):
            print "not validated"
            return False
            # user = User.query.find(username = self.username)
            # print user
            # if user:
            #   self.username.errors.append("Username taken")
            #  return False
        return True


class RegisterForm(Form):
    username = StringField('Username', [InputRequired("please enter a username")])
    password = PasswordField('Password', [InputRequired("please enter a password"),
                                          EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Password Again', [InputRequired("type your password again")])

    def validate_on_submit(self):
        if not Form.validate(self):
            print "not validated"
            return False

        return True


class SettingForm(Form):
    displayName = StringField('Display Name')
    date = DateTimeField('Notification Time')
    notification = BooleanField('Turn on Notifications')
    public = BooleanField('See all posts')
    # public = BooleanField('Make my posts public')
