''' sql_test '''
import mysql.connector
from mysql.connector import errorcode

def get_conn():
    ''' returns the database connection '''
    try:
        conn = mysql.connector.connect(
            user='root',
            password='example',
            host='127.0.0.1',
            database='test')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    return conn


def get_cursor():
    ''' return the cursor '''
    conn = get_conn()
    print(f'{conn}')
    return conn.cursor()


def create_user(first_name, last_name):
    ''' Create a new user '''

    add_user = (
        'INSERT into users '
        '(firstName, lastName) '
        'VALUES (%s, %s)'
    )
    user_data = (first_name, last_name)
    cursor = get_cursor()
    cursor.execute(add_user, user_data)


def get_all_users():
    ''' get all users in database '''
    query = ("SELECT firstName, lastName FROM users ")
    
    get_conn().cursor().execute(query)
    cursor = get_cursor()
    cursor.execute(query)

    print('Here')
    # Iterate through the cursor and print each user
    for (first_name, last_name) in cursor:
        print(f"{first_name} {last_name}")


get_all_users()
