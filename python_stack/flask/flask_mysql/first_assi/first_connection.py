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

# # 1
# @app.route('/')
# def index():
#     mysql = connectToMySQL("first_flask")
#     friends = mysql.query_db("SELECT * FROM friends;")
#     print(friends)
#     return render_template("index.html", all_friends = friends)

# <h1>All My Friends</h1>
# {% for one_friend in all_friends %}
#     <p>First Name: {{one_friend["first_name"]}}</p>
#     <p>Last Name: {{one_friend["last_name"]}}</p>
#     <p>Occupation: {{one_friend["occupation"]}}</p>
#     <hr>
# {% endfor %}

# # 2
# query="UPDATE friends SET first_name=%(fn)s WHERE id=%(id_num)s;"
# data = {
#     'fn': #possibly a value from a form,
#     'id_num': #possibly a value from the url,
# }
# mysql.query_db(query, data)

# # 3
# <h1>Add a Friend</h1>
# <form action="/create_friend" method="POST">
#     <p>First Name: <input type="text" name="fname"></p>
#     <p>Last Name: <input type="text" name="lname"></p>
#     <p>Occupation: <input type="text" name="occ"></p>
#     <input type="submit" value="Add Friend">
# </form>

# @app.route("/create_friend", methods=["POST"])
# def add_friend_to_db():
    # mysql= connectToMySQL('first_flask')

    # print(request.form)
    #   QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #   VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
    #     data={
    #         'fn':request.form['fname'],
    #         'ln':request.form['lname'],
    #         'occup':request.form['occ']
    #     }
    #     new_friend_id = mysql.query_db(query, data)
    #     return redirect('/')