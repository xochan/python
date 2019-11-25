from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'message' not in session:
        session['message'] = []
    return render_template("index.html", gold = session['gold'], mess = session['message'])

@app.route('/process_money', methods=['POST'])
def process():
    session['value'] = request.form['pro']
    print(request.form)
    if 'gold' not in session:
        session['gold'] = 0
    if 'message' not in session:
        session['message'] = []
    if session['value'] == 'farm':
        print(session['gold'])
        num = random.randint(10,20)
        session['message'].append(["earned "+str(num)+" in farm","red"])
        session['color']='red'
        session['gold'] += num
        print('+',num,'= ',session['gold'], '\n',"*"*40)
    if session['value'] == 'cave':
        print(session['gold'])
        num = random.randint(5,10)
        session['message'].append(["earned "+str(num)+" in cave","red"])
        session['color']='red'
        session['gold'] += num
        print('+',num,'= ',session['gold'], '\n',"*"*40)
    if session['value'] == 'house':
        print(session['gold'])
        num = random.randint(2,5)
        session['message'].append(["earned "+str(num)+" in house","red"])
        session['color']='red'
        session['gold'] += num
        print('+',num,'= ',session['gold'], '\n',"*"*40)
    if session['value'] == 'casino':
        print(session['gold'])
        i = random.randint(1,2)
        if i == 1:
            print('earn')
            num = random.randint(0,50)
            session['message'].append(["earned "+str(num)+" in casino","red"])
            session['color']='red'
            session['gold'] +=num 
            print('+',str(num),'= ',session['gold'], '\n',"*"*40)
        if i == 2:
            print('take')
            num = random.randint(0,50)
            session['message'].append(["take"+str(num)+" in casino","black"])
            session['color']='black'
            session['gold'] -= num
            print('+',str(num),'= ',session['gold'], '\n',"*"*40)
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('message')
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)