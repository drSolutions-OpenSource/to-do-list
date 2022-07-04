from ConfigureAndUseStore import *


class ToDoList:
    store = ConfigureAndUseStore('', '')

    def __init__(self, filename, file_path):
        self.store = ConfigureAndUseStore(filename, file_path)

    def add_activity(self, title, description):
        """Insert one activity

        :param title: Activity title
        :param description: Activity description
        :return: True on success, False if insert does not occur
        """
        return self.store.insert_activity(title, description)

    def update_activity(self, id_activity, title, description):
        """Update activity

        :param id_activity: Activity identifier
        :param title: Activity title
        :param description: Activity description
        :return: True on success, False if update does not occur
        """
        return self.store.update_activity(id_activity, title, description)

    def select_activity(self, id_activity, complete=True):
        """Select an activity

        :param id_activity: Activity identifier
        :param complete: True to display all attributes, or False to just title and description
        :return:
        """
        if self.store.select_activity(id_activity):
            self.print_activity(self.store.lines[0], complete)
            return True
        else:
            print('Identifier not found!\n')
            return False

    def delele_activity(self, id_activity):
        """Delete an activity

        :param id_activity: Activity identifier
        :return: True on success, False if delete does not occur
        """
        return self.store.delete_activity(id_activity)

    @staticmethod
    def print_activity(line, complete=True):
        """Display an activity

        :param line: Line with activity information
        :param complete: True to display all attributes, or False to just title and description
        """
        if complete:
            print(f'Identifier .. = {line[0]}')
            print(f'Title ....... = {line[1]}')
            print(f'Description.. = {line[2]}')
            print(f'Date ........ = {line[3]}\n')
        else:
            print(f'Title ....... = {line[1]}')
            print(f'Description.. = {line[2]}\n')

    def select_all_activities(self):
        """Select all activities in the database showing its data
        """
        self.store.select_all_activities()
        if self.store.lines is None:
            print('No activities!')
        else:
            if len(self.store.lines) > 0:
                for line in self.store.lines:
                    self.print_activity(line)
            else:
                print('No activities!')

    def close_store(self):
        """Close the connection to the database
        """
        self.store.close_database()
