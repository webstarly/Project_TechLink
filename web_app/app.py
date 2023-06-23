from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    return ("TechLink")

@app.route('/home', strict_slashes=False)
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(0)
