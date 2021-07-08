from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    request_form = request.form
    count = int(request_form['strawberry']) + int(request_form['raspberry']) + int(request_form['apple'])
    print("Charging" , request_form['first_name'] , "for" , count , "fruits")
    return render_template("checkout.html", request_form=request_form)

@app.route('/fruits')         
def fruits():
    fruit = [
        'apple.png',
        'blackberry.png',
        'raspberry.png',
        'strawberry.png'
    ]
    return render_template("fruits.html", fruits=fruit)

if __name__=="__main__":   
    app.run(debug=True)    