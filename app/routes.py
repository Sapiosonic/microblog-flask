from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Rada'}
	return render_template('index.html', title='Home', user=user) # type: ignore

