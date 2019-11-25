from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def box():
    return render_template('play.html')

@app.route('/play/<x>')
def repeat(x):
    return render_template('play1.html', time=int(x))

@app.route('/play/<x>/<color>')
def color(x,color):
    return render_template('play2.html', time=int(x), color= color)

if __name__ == "__main__":
    app.run(debug=True)