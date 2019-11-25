from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

@app.route('/')
def index():
    number = random.randint(1,100)
    print(number)
    print(session['guess'])
    print(request.form)
    if number == session['guess']:
        print('equal, u win')
    if number > session['guess']:
        print('too low!')
    if number < session['guess']:
        print('too high!')
    return render_template("index.html",number = number, guess = session['guess'])

# @app.route('/')
# def index():
#     return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    session['guess'] = int(request.form['num'])
    print(request.form)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)