from flask import Flask
from flask import url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    print(url_for('variable', num=8))
    # storing and accesing static files
    image = url_for('static', filename='test.jpg')
    return render_template("home.html")


#variable routes and jinja
@app.route('/variable/<int:num>')
def variable(num):
    return f"<h1>{num}</h1>"

# managing get and post requests
@app.route('/login',methods=['GET','POST'])
def login():
    req = request.method
    ourput_text = req
    if req =="POST":
        return f"<h1>POST</h1>"
    else:
        return f"<h1>{req}</h1>"

# managing get and post in separate functions
@app.post('/submit')
def submit():
    print(request.method)
    return f"<h1>only post request can access this function</h1>"

@app.route('/home')
def main():
    return render_template('home.html', name='Haresh')
@app.route('/consultation')
def schedule():
    return render_template("meeting.html")

@app.route('/about')
def about():
    return render_template('about.html')



while True:
    app.run("localhost","8080",debug=True)


