from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user data (replace this with a database in a real application)
users = {
    'Nag': '3609',
    'sai': '4100'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f"Welcome,To the world,{username}!"
    else:
        return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
