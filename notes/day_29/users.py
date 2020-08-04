''' sql_test '''
import mysql.connector
from mysql.connector import errorcode


class Users():
    ''' Users class '''
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user='root',
                password='example',
                host='127.0.0.1',
                database='test')
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close_db(self):
        ''' close the database '''
        self.conn.close()

    def create_user(self, first_name, last_name):
        ''' Create a new user '''

        add_user = (
            'INSERT into users '
            '(firstName, lastName) '
            'VALUES (%s, %s)'
        )
        user_data = (first_name, last_name)
        self.cursor.execute(add_user, user_data)
        self.conn.commit()

    def get_all_users(self):
        ''' get all users in database '''
        query = ("SELECT firstName, lastName FROM users ")
        self.cursor.execute(query)

        # Iterate through the cursor and print each user
        for (first_name, last_name) in self.cursor:
            print(f"{first_name} {last_name}")


/games/{id}/move
{
    "row": 2,
    "column": 4,
    "player": 1
}