from datetime import datetime
from utilities.db_connection import fetchall, fetchone, insertone
from utilities.generate_new_id import generate_new_id_by_firstname_lastname, generate_new_id_by_username_lastname

def get_all_users():
        sql_statement = 'SELECT * FROM user'
        res = fetchall(sql_statement)
        print(res)

def get_user_by_id(id):
        sql_statement = 'SELECT * FROM user WHERE id_user = %(id)s'
        res = fetchone(sql_statement, id)
        print(res)

def get_user_by_firstname_and_lastname(attributes):
        sql_statement = 'SELECT * FROM user WHERE Firstname = %(Firstname)s AND Lastname = %(Lastname)s'
        res = fetchone(sql_statement, attributes)
        print(res)

# TODO: Check how to rollback if doing it with transaction
def post_new_user(attributes):
        try:
                attributes["IdUser"] = str(generate_new_id_by_firstname_lastname(attributes))
                attributes["Created"] = datetime.now().isoformat()
                
                sql_statement_for_user = '''INSERT INTO user (idUser, Lastname, Firstname, DateInserted, DateUpdated, Username) 
                                                        VALUES (%(IdUser)s, %(Lastname)s, %(Firstname)s, %(Created)s, %(Created)s, %(Username)s)'''
                status = insertone(sql_statement_for_user, attributes)
        except:
                status = False

        if status:
                try:
                        attributes["IdLogin"] = str(generate_new_id_by_username_lastname(attributes))
                        print("Login OK")
                        sql_statement_for_userlogin = '''INSERT INTO userlogin (idUserLogin, Username, Password)
                                                                VALUES (%(IdLogin)s, %(Username)s, %(Password)s)'''
                        status = insertone(sql_statement_for_userlogin, attributes)
                        print(status)
                except:
                        raise ValueError("Error generating user for person.")
        else:
                raise ValueError("Error inserting person.")

# Test cases
# get_user_by_id({'id':'a3f1b5ee-7484-371e-be6a-c7154904667b'})
# get_user_by_firstname_and_lastname({'Firstname':'Luca','Lastname':'Mustermann'})
# post_new_user({'Firstname':'Ruggero','Lastname':'De Ceglie', 'Username':'daiC','Password':'Password'})
