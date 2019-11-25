
import pymysql.cursor ## mistype pymysql.cursors or forget import it

class MySQLConnection
    def __init__(self, db) ### forget to put colon after methods or if else or in class
        connection = pymysql.connect(host = 'localhost',
                                    port = 9090,
                                    user = 'root', 
                                    password = 'fsafgfsg', ### wrong password
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)

        # self.connection = connection <= missing connection

    def query_db(self, query, data=None)
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0

                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0

                    result = cursor.fetchall()
                    return result
                else:

                    self.connection.commit()
            except Exception as e

                print("Something went wrong", e)
                return False

                # you forget to close the connection

# forget to the methos below
# def connectToMySQL(db)
#     return MySQLConnection(db)