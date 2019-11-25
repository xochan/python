from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def pick():
    print('run')
    print(request.form)
    name = request.form['name']
    state = request.form['state']
    comment = request.form['comment']
    language= request.form['language']

    return render_template('result.html',name=name, state=state, comment=comment, language=language)

if __name__ == "__main__":
    app.run(debug=True)