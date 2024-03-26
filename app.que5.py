from flask import Flask, session,redirect,url_for

app = Flask(__name__)
app.secret_key = b'Shivdatta@1' #key for session encryption

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]} <br> <a href="/logout">Logout</a>'
    return 'You are not logged in <br> <a href="/login">Login</a>'

@app.route('/login')
def login():
    session['username'] = 'user123'
    return redirect (url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect (url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
