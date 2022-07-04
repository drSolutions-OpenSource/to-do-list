from ToDoList import *
from MainScreen import *


if __name__ == '__main__':
    tdl = ToDoList('', '')
    ms = MainScreen()

    ms.header()

    while True:
        ms.menu()
        option = ms.get_option()

        if option == 1:
            print('-' * 17 + ' All activities ' + '-' * 17 + '\n')
            tdl.select_all_activities()
        elif option == 2:
            print('-' * 17 + ' Show activity ' + '-' * 18 + '\n')
            id = input('Identifier: ')
            print('')
            tdl.select_activity(id)
        elif option == 3:
            print('-' * 17 + ' Include activity ' + '-' * 15 + '\n')
            title = input('Title .....: ')
            description = input('Description: ')
            tdl.add_activity(title, description)
            print('\nDone!\n')
        elif option == 4:
            print('-' * 17 + ' Update activity ' + '-' * 16 + '\n')
            id = input('Identifier: ')
            print('')
            if tdl.select_activity(id, False):
                title = input('Title .....: ')
                description = input('Description: ')
                tdl.update_activity(id, title, description)
                print('\nDone!\n')
        elif option == 5:
            print('-' * 17 + ' Delete activity ' + '-' * 16 + '\n')
            id = input('Identifier: ')
            print('')
            if tdl.select_activity(id, False):
                tdl.delele_activity(id)
                print('Done!\n')
        elif option == 6:
            break
        else:
            print('Invalid option!\n')

        input('Press <ENTER>...')

    tdl.close_store()
