from flask import Flask, abort 

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return 'Caught 404 error: make sure you are accessing proper method '

@app.errorhandler(500)
def internal_server_error(error):
    return 'Caught 500 error: Internal server error please check input'

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/error')
def error():
    abort(500)

if __name__ == '__main__':
    app.run(debug=True)
