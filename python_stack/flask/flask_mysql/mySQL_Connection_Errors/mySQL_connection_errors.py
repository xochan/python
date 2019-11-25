from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    # call the function, passing in the name of our db
    mysql = connectToMySQL('friends')	        
    # call the query_db function, pass in the query as a string
    user = mysql.query_db('SELECT * FROM users;')  
    # call the query_db function, pass in the query as a string
    print(user)
    return str(user)
if __name__ == "__main__":
    app.run(debug=True)