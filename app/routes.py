from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Akif'}
	posts = [
		{
			'author' : {'username' : 'egemen'},
			'body' : 'Sennn Cidddi misiiiinn?'
		},
		{
			'author' : {'username' : 'gazoz'},
			'body' : 'Fısssss!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts = posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('index'))

