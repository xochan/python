from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def _8by8():
    return render_template('checker_board.html')

@app.route('/<x>')
def _8byX(x):
    return render_template('checker_board1.html',square=int(x))

@app.route('/<x>/<y>')
def _XbyY(x,y):
    return render_template('checker_board2.html',col=int(x),row=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def color(x,y,color1,color2):
    return render_template('checker_board3.html',col=int(x),row=int(y),mau1=color1, mau2=color2)

if __name__ == "__main__":
    app.run(debug=True)

    