import sys


def main():
    shopping_list = ['apples', 'bananas', 'oranges']
    while True:
        print_menu()
        choice = input('What do you want to do? ')
        handle_user_input(choice, shopping_list)


def print_menu():
    print('-------------------------------------------')
    print('             SHOPPING LIST')
    print('-------------------------------------------')
    print()
    print('(1) Show list')
    print('(2) Add item')
    print('(3) Delete item')
    print('(4) Edit item')
    print('(5) Quit')
    print()


def handle_user_input(choice, shopping_list):
    switcher_ = {
        '1': lambda: show_list(shopping_list),
        '2': lambda: add_item(),
        '3': lambda: delete_item(),
        '4': lambda: edit_item(),
        '5': lambda: quit_()
    }

    return switcher_.get(choice, lambda: "Invalid choice, please enter a number between 1 and 5!")()


def show_list(shopping_list):
    print('Your shopping list:')
    [print('-{}'.format(item)) for item in shopping_list]
    print()
    show_press_enter_message()


def add_item():
    pass


def delete_item():
    pass


def edit_item():
    pass


def quit_():
    print('Bye bye!!!')
    sys.exit()


def show_press_enter_message():
    input("Press Enter to continue...")


if __name__ == '__main__':
    main()
