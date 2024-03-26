from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to home page, please select /user/put user name to move further '



@app.route('/user/<username>')
def user_profile(username):
    users = {
        'shiv': {'name': 'shiv', 'age': 30, 'occupation': 'ML Engineer'},
        'datta': {'name': 'Datta', 'age': 25, 'occupation': 'DS Teacher'}
    }
    if username in users:
        user_info = users[username]
        return render_template('index.html', user_info=user_info)
    else:
        return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
