from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')                           
def index():
    return render_template('index.html') 
@app.route('/play/')
def play():
    return render_template('index.html', times=3, color='blue', content='center')
@app.route('/play/<num>')
def playnum(num):
    num = int(num)
    cont = 'none'
    if num < 4:
        cont = 'center'
    return render_template('index.html', color='blue', times=num, content=cont)
@app.route('/play/<num>/<color>')
def playnumcolor(num, color):
    num = int(num)
    cont = 'none'
    if num < 4:
        cont = 'center'
    return render_template('index.html', color=color, times=num, content=cont)

if __name__=="__main__":      
    app.run(debug=True)    




