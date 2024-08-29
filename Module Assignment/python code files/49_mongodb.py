from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']  
users = db['users']     

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        existing_user = users.find_one({'username': username})

        if existing_user is None:
            # Hash the password
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Insert user into the database
            users.insert_one({'username': username, 'password': hashed_pw})
            session['username'] = username
            return redirect(url_for('welcome'))
        
        return 'Username already exists! Try a different one.'

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Find user in the database
        user = users.find_one({'username': username})

        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                session['username'] = username
                return redirect(url_for('welcome'))
        
        return 'Invalid username or password!'
    
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"Hello, {session['username']}! Welcome to Geeks!"
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
