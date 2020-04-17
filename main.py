from flask import render_template
from flask import Flask
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'calculator'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/user')
def signup():
  form = SignUpForm()
  return render_template('user.html',form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

