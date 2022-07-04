from os.path import exists
import sqlite3
from datetime import date


class ConfigureAndUseStore:
    database_file = ''
    conn = None
    lines = None

    def __init__(self, filename, file_path):
        if len(filename):
            self.file_name = filename
        else:
            self.file_name = 'activities.db'
        if len(file_path):
            self.file_path = file_path
        else:
            self.file_path = './'
        self.database_file = self.file_path + self.file_name

        if exists(self.database_file):
            self.load_database(True)
        else:
            self.load_database(False)

    def load_database(self, file_exist):
        """Load the database to the system

        :param file_exist: Informs if the file already exists
        """
        try:
            self.conn = sqlite3.connect(self.database_file)
            if not file_exist:
                self.create_activities_table()
        except sqlite3.OperationalError as error:
            exit(f'Unable to open database file - Error: {error}')

    def create_activities_table(self):
        """Create the table in the database
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE activities (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                date_activity DATE NOT NULL
        );
        """)

    def close_database(self):
        """Close the connection to the database
        """
        self.conn.close()

    def insert_activity(self, title='', description=''):
        """Insert one activity in the database

        :param title: Activity title
        :param description: Activity description
        :return: True on success, False if insert does not occur
        """
        if (len(title) == 0) or (len(description)) == 0:
            return False
        cursor = self.conn.cursor()
        today = date.today()
        date_dabatase = today.strftime('%Y-%m-%d')
        query = f"""
        INSERT INTO activities (title, description, date_activity) 
        VALUES ('{title}', '{description}', '{date_dabatase}')
        """
        cursor.execute(query)
        self.conn.commit()
        return True

    def update_activity(self, id_activity='', title='', description=''):
        """Update activity in the database

        :param id_activity: Activity identifier
        :param title: Activity title
        :param description: Activity description
        :return: True on success, False if update does not occur
        """
        if (len(id_activity) == 0) or (len(title) == 0) or (len(description)) == 0:
            return False
        cursor = self.conn.cursor()
        today = date.today()
        date_dabatase = today.strftime('%Y-%m-%d')
        query = f'UPDATE activities SET title=\'{title}\', description=\'{description}\', ' \
                f'date_activity = \'{date_dabatase}\' WHERE id = {id_activity}'
        cursor.execute(query)
        self.conn.commit()
        return True

    def delete_activity(self, id_activity=''):
        """Delete activity in the database

        :param id_activity: Activity identifier
        :return: True on success, False if delete does not occur
        """
        if len(id_activity) == 0:
            return False
        cursor = self.conn.cursor()
        query = f'DELETE FROM activities WHERE id = {id_activity}'
        cursor.execute(query)
        self.conn.commit()
        return True

    def select_activity(self, id_activity):
        """Select an activity in the database returning its data

        :param id_activity: Activity identifier
        :return: True on success, False if the user enters an invalid identifier
        """
        if len(id_activity) == 0:
            return False
        cursor = self.conn.cursor()
        query = f'SELECT count(id) FROM activities WHERE id = {id_activity} LIMIT 1'
        qtd_rows = cursor.execute(query).fetchone()[0]
        if qtd_rows:
            query = f'SELECT id, title, description, date_activity FROM activities WHERE id = {id_activity} LIMIT 1'
            cursor.execute(query)
            self.lines = cursor.fetchall()
            return True
        return False

    def select_all_activities(self):
        """Select all activities in the database returning its data

        :return: True if there are activities, False otherwise
        """
        cursor = self.conn.cursor()
        query = f'SELECT count(id) FROM activities'
        qtd_rows = cursor.execute(query).fetchone()[0]
        if qtd_rows:
            query = f'SELECT id, title, description, date_activity FROM activities ORDER BY id'
            cursor.execute(query)
            self.lines = cursor.fetchall()
            return True
        return False
