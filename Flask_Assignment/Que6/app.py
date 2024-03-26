from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display', methods = ['POST'])
def display():
    user_input = request.form['userInput']
    return render_template('display.html',user_input = user_input)


if __name__ == '__main__':
    app.run(debug=True)







