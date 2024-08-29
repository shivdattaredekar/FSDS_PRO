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
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

credentials = {
    'shiv': 'shivdatta@1',
    'aman': 'april@2024',
    'debu': 'Planning@2023',
    'priya': 'Planning@2024',
    'yash': 'Ready@2023'
}

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        if name in credentials and credentials[name] == password:
            return f'Welcome {name}! You have successfully logged in.'
        else:
            return 'Invalid credentials, please try again.'

    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True, port= 5005)