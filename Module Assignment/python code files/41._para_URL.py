from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return f'Welcome to our website, {name}!'

if __name__ == '__main__':
    app.run(debug=True, port = 5002)