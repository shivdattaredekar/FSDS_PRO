from flask import Flask, request, render_template_string


app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form method="POST" action="/">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Thank you {name} for submitting your information. Your email address is {email}.'
    else:
        return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True, port= 5000)