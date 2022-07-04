class MainScreen:
    def __init__(self):
        pass

    @staticmethod
    def header():
        """Display the header
        """
        print('=' * 50 + '\n' + 'To Do List'.center(50) + '\n' + '=' * 50)

    @staticmethod
    def menu():
        """Display the menu of options
        """
        print("""\n1 - View all activities
2 - Show only one activity
3 - Include activity
4 - Update activity
5 - Delete activity
6 - Exit system\n""")

    @staticmethod
    def get_option():
        """Request the option to the user

        :return: User option
        """
        option = int(input('Option: '))
        print('')
        return option
