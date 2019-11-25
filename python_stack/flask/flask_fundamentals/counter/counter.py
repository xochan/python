from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form



@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    print(session['count'])
    if 'count' in session:
        session['count']+=1
    if 'real' not in session:
        session['real'] = 0
    if 'real' in session:
        session['real']+=1
    print(session['count'])
    print(request.form)
    return render_template("index.html")

@app.route('/destroy')
def destroy():
    session.pop('count')
    return redirect('/')

@app.route('/add2')
def add2():
    session['count']+=1
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    session['count']+=int(request.form['num'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)