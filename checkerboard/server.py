from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')                           
def index():
    r = 8
    col = 8
    colr1 = 'red'
    colr2 = 'black'
    return render_template('index.html', column=col, row=r, color1=colr1, color2=colr2) 

@app.route('/4')
def four():
    r =4
    col = 8
    colr1 = 'red'
    colr2 = 'black'
    return render_template('index.html', column=col, row=r, color1=colr1, color2=colr2)

@app.route('/<row>/<column>/')
def xandy(row, column):
    r = int(row)
    col = int(column)
    colr1 = 'red'
    colr2 = 'black'
    return render_template('index.html', column=col, row=r, color1=colr1, color2=colr2)

@app.route('/<row>/<column>/<color1>/<color2>')
def xandyc1c2(row, column, color1, color2):
    r = int(row)
    col = int(column)
    colr1 = color1
    colr2 = color2
    return render_template('index.html', column=col, row=r, color1=colr1, color2=colr2)


if __name__=="__main__":      
    app.run(debug=True)    




