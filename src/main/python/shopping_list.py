import collections
import sys


def main():
    shopping_list = load_shopping_list()
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
        '1': lambda: show_list(shopping_list, 'Y'),
        '2': lambda: add_item(shopping_list),
        '3': lambda: delete_item(shopping_list),
        '4': lambda: edit_item(shopping_list),
        '5': lambda: quit_()
    }

    return switcher_.get(choice, lambda: "Invalid choice, please enter a number between 1 and 5!")()


def show_list(shopping_list, show_press_enter):
    print()
    print('Your shopping list:')
    print('--------------------------')
    print('Item           | Quantity')
    print('--------------------------')
    [print('{}{}| {}'.format(item.name, return_white_spaces(15, item.name), item.quantity)) for
     item in
     shopping_list]
    print()
    if show_press_enter == 'Y':
        show_press_enter_message()


def add_item(shopping_list):
    name = input('Item name: ')
    quantity = input('Quantity: ')
    Item = collections.namedtuple('Item', 'name quantity')
    new_item = Item(name=name, quantity=quantity)
    shopping_list.append(new_item)
    print()
    print('{} added to shopping list.'.format(new_item.name))
    show_list(shopping_list, 'N')
    print()
    show_press_enter_message()


def delete_item(shopping_list):
    show_list(shopping_list, 'N')
    print()
    item_name_to_remove = input('Item to remove: ')
    try:
        item_to_remove = [item for item in shopping_list if item.name == item_name_to_remove][0]
    except IndexError as ie:
        print("Item {} doesn't exist in the list.".format(item_name_to_remove))
    else:
        shopping_list.remove(item_to_remove)
        print('{} removed from the shopping list.'.format(item_name_to_remove))
    show_list(shopping_list, 'N')
    print()
    show_press_enter_message()


def edit_item(shopping_list):
    show_list(shopping_list, 'N')
    print()
    item_name_to_edit = input('Item to edit: ')
    try:
        item_to_edit = [item for item in shopping_list if item.name == item_name_to_edit][0]
    except IndexError as ie:
        print("Item {} doesn't exist in the list.".format(item_name_to_edit))
    else:
        new_name = input('Enter new name or press enter to keep the same name: ')
        new_name = item_to_edit.name if (len(new_name) == 0) else new_name
        new_quantity = input('Enter new quantity or press enter to keep the same quantity: ')
        new_quantity = item_to_edit.quantity if (len(new_quantity) == 0) else new_quantity
        index = shopping_list.index(item_to_edit)
        Item = collections.namedtuple('Item', 'name quantity')
        shopping_list[index] = Item(name=new_name, quantity=new_quantity)
        print()
        print('Shopping list updated.')
    show_list(shopping_list, 'N')
    print()
    show_press_enter_message()


def quit_():
    save_shopping_list()
    print('Bye bye!!!')
    sys.exit()


def show_press_enter_message():
    input("Press Enter to continue...")


def load_shopping_list():
    Item = collections.namedtuple('Item', 'name quantity')
    apples = Item(name='apples', quantity=5)
    bananas = Item(name='bananas', quantity=3)
    oranges = Item(name='oranges', quantity=2)
    shopping_list = [apples, bananas, oranges]
    return shopping_list


def save_shopping_list():
    pass


def return_white_spaces(length, string):
    return ' ' * (length - len(string))


if __name__ == '__main__':
    main()
