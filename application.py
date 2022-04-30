from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

form = []
userData = {}

def string_separator(string:str):
    newString = ""
    newString += string[0].capitalize()
    for i in range(1, len(string)):
        if string[i].isupper():
            newString += " "
        newString += string[i]
    return newString

class FormItem():
    def __init__(self, name, placeholder, typef = "text") -> None:
        self.title = string_separator(name)
        self.name = name
        self.typef = typef
        self.placeholder = placeholder

form.append(FormItem("name", "Enter your name"))
form.append(FormItem("lastName", "Enter your last name"))
form.append(FormItem("username", "Enter your username"))
form.append(FormItem("email", "Enter your name", "email"))
form.append(FormItem("password", "Enter your password", "password"))
form.append(FormItem("dateOfBirth", "Enter your date of birth", "date"))

@app.route('/', methods=['GET', ])
def index():
    if request.method == 'POST':
        return redirect(url_for('profile'))
    return render_template('index.html', fields=form)

@app.route('/profile', methods=['POST'])
def profile():
    user = {}
    for key, value in request.form.items():
        user[string_separator(key)] = value
    return render_template('profile.html', fields=user)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    