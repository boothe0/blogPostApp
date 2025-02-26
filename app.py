from urllib import request

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# Set a secret key for encrypting session data
app.secret_key = 'my_secret_key'

# dictionary to store user and password
users = {
    'elizabethbooth05@gmail.com': '1234',
    'user2': 'password2'
}
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/handleLogin', methods=['POST'])
def handle_login():
    if request.method == 'POST':
        username = request.form['emailPremade']
        print(username)
        if username in users:
            return render_template('blogger.html', first_name=username)
        else:
            return render_template('login_form.html')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        print(username, password)
        if username in users and users[username] == password:
            return render_template('blogger.html', first_name=first_name)
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login_form.html')

@app.route('/login')
def login_page():
    return render_template('login_form.html', title='Login Page')

@app.route('/blogger')
def blogger_main_page():
    return render_template('blogger.html')

if __name__ == '__main__':
    app.run()
