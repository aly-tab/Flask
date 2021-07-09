from flask import Flask, render_template, request, redirect, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'VKX47&%DLP09A@#1x'

randInt = random.randint(1,100)
display1 = 'none'
display2 = 'none'

@app.route('/')
def index():
    global display1
    global display2
    return render_template("index.html", display1=display1, display2=display2)

@app.route('/check', methods=['POST'])
def check():
    print(request.form)
    request_form = request.form
    guess = int(request_form['guess'])
    global randInt
    session['number'] = randInt
    global display1
    global display2
    color = 'red'
    if session['number'] == guess:
        string = str(guess) + " was the number!"
        display2 = 'block'
        color = 'green'
    elif session['number'] > guess:
        string = "Too low"
        display1 = 'block'
    elif session['number'] < guess:
        string = "Too High"
        display1 = 'block'

    return render_template("index.html", user_guess=string, display1=display1, display2=display2, color=color)

@app.route('/reset', methods=['POST'])
def reset():
    global randInt
    global display1
    global display2

    display1 = 'none'
    display2 = 'none'
    session.clear()
    randInt = random.randint(1,100)

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)