import datetime
from colorama import Fore, Style

from controller import Controller
from modelJSON import ModelJSON
from note import Note
from view import View


def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(Fore.BLUE +
                        '1 - Создать заметку\n'
                        '2 - Прочитать заметку\n'
                        '3 - Обновить заметку\n'
                        '4 - Удалить заметку\n'
                        '5 - Удалить все заметки\n'
                        '6 - Прочитать все заметки\n'
                        '7 - Выход\n' +
                        'Что Вы хотите сделать?: '
                        + Style.RESET_ALL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + '\nСоздать заметку:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            print(Fore.GREEN + '\nПрочитать заметку:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + '\nОбновить заметку:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить заметку:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '5':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить все заметки:' + Style.RESET_ALL)
                if input(Fore.RED + 'Вы точно хотите удалить все заметки? (Y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '6':
            if c.notes_exist():
                print(Fore.BLUE + '\nСписок всех заметок:' + Style.RESET_ALL)
                c.show_notes()
        else:
            print(Fore.RED + 'Команда введена неверно' + Style.RESET_ALL)


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'id введено неверно' + Style.RESET_ALL)
