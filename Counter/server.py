from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret key for counter'

counter = 0

@app.route('/')
def index():
    global counter
    counter = counter + 1
    session['number'] = counter
    return render_template("index.html", number=session['number'])

@app.route('/by_two', methods=['POST'])
def by_two():
    global counter
    counter =  counter + 1
    session['number'] = counter
    return redirect(url_for('index', number=session['number']))

@app.route('/reset', methods=['POST'])
def reset():
    global counter
    counter = 0
    session['number'] = counter
    return redirect(url_for('index', number=session['number']))

@app.route('/destroy_session')
def destroy_session():
    global counter 
    session.clear()
    counter = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)