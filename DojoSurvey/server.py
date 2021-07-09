from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'VKX47&ASYFG56209A@#1x'



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['form'] = request.form
    return redirect("/result")


@app.route('/result')
def result():
    return render_template('result.html')



if __name__=="__main__":
    app.run(debug=True)

