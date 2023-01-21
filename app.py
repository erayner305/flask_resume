from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Johns"
    return render_template('index.html', 
        f_name = first_name)

@app.route('/about')
def about():
    first_name = "Easton"
    return render_template('about.html', f_name = first_name)


