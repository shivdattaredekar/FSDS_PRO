from flask import Flask, render_template_string, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define a form class using Flask-WTF
class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Submit')

form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span><br>
            {% endfor %}
        </div>
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span><br>
            {% endfor %}
        </div>
        <div>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
                <span style="color: red;">[{{ error }}]</span><br>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the form data
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Here you could save the data to the database or perform other actions
        return redirect(url_for('success'))

    return render_template_string(form_html, form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=8001)
