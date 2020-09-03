from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods= ['GET'])
def landing():
    return render_template('index.html',)

@app.route('/', methods = ['POST'])
def action():
    try:
        text = request.form['text'].lower()
        key = request.form['key'].lower()
    except:
        return redirect("/")
    if request.form.get('decrypt'):
        res = decrypt(text, key, 26)
    else:
        res = encrypt(text, key, 26)
    return render_template('index.html', text = text, key = key, res = res)

def decrypt(p, k, m):
    res = ""
    for i in range(len(p)):
        c = ord(p[i]) - 97
        s = ord( k[ (i%len(k)) ] ) - 97
        res  += chr(  (c-s+26) % m  + 97 )
    return res

def encrypt(p, k, m):
    res = ""
    for i in range(len(p)):
        f = ord(p[i]) - 97
        s = ord( k[ (i%len(k)) ] ) - 97
        res  += chr(  (f+s) % m  + 97 )
    return res


if __name__ == '__main__':
    app.run(debug=True)