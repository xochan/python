from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)

@app.route('/')
def op():
    return render_template('random.html')

@app.route('/pick', methods=['POST'])
def pick():
    cpu = round(random.random()*3)
    print('cpu chose:',cpu)
    userChoice = int(request.form['choice'])
    print('user chose:',userChoice)
    if cpu == userChoice:
        print('tie')
        return render_template('tie.html')
    elif userChoice == 1 and cpu != 2:
        print('win')
        return render_template('win.html')
    elif userChoice == 2 and cpu != 3:
        print('win')
        return render_template('win.html')
    elif userChoice == 3 and cpu != 1:
        print('win')
        return render_template('win.html')
    else:
        print('lose')
        return render_template('lose.html')

# @app.route('/play/<x>/<color>')
# def color(x,color):
#     return render_template('play2.html', time=int(x), color= color)

if __name__ == "__main__":
    app.run(debug=True)