import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from flask import session
import bcrypt
from models import User, Attendance, Event
from forms import RegisterForm, LoginForm, CommentForm

app = Flask(__name__)  # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context



@app.route('/')
@app.route('/home')
def home()




@app.route('/events')
def events()





@app.route('/events/<note_id>')
def get_events(note_id)




@app.route('/events/new', methods=['GET', 'POST'])
def new_event()



@app.route('/events/edit/<note_id>', methods=['GET', 'POST'])
def update_event()


@app.route('/events/rsvp')
def rsvp_event()


@app.route('/events/delete/<note_id>', methods=['POST'])
def delete_event(note_id):
    # check if a user is saved in session
    if session.get('user'):
        # retrieve events from database
        my_event = db.session.query(events).filter_by(id=note_id).one()
        db.session.delete(my_event)
        db.session.commit()

        return redirect(url_for('get_events'))
    else:
        # user is not in session redirect to login
        return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create user model
        new_user = User(first_name, last_name, request.form['email'], h_password)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user'] = first_name
        session['user_id'] = new_user.id # access id value from user model of this newly added user
        # show user dashboard view
        return redirect(url_for('get_events'))

    # something went wrong - display register view
    return render_template('login/signup.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            # render view
            return redirect(url_for('get_events'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login/signup.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login/signup.html", form=login_form)



@app.route('/logout')
def logout():
    # check if a user is saved in session
    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)