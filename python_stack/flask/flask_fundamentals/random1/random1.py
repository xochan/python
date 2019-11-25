from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)

@app.route('/')
def op():
    return render_template('random.html')

@app.route('/pick', methods=['POST'])
def pick():
    cpu = round(random.random()*3)
    rock1 = request.form['rock']
    paper2 = request.form['paper']
    scissors3 = request.form['scissors']
    rock1=int(1)
    paper2=int(2)
    scissors3=int(3)
    if cpu == (rock1 or paper2 or scissors3):
        return render_template('random1.html')
    else:
        return render_template('random2.html')


# @app.route('/play/<x>/<color>')
# def color(x,color):
#     return render_template('play2.html', time=int(x), color= color)

if __name__ == "__main__":
    app.run(debug=True)