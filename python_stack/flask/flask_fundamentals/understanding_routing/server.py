from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    print('hello world')
    return 'hello world'

@app.route('/dojo')
def say_dojo():
    return 'dojo'

@app.route('/say/<name>')
def say_name(name):
    return 'hi '+ str(name) 

@app.route('/repeat/<id>/<action>')
def repeat(id,action):
    return (str(action)+"\n"+"\n" )* int(id)

if __name__ == "__main__":
    app.run(debug=True)