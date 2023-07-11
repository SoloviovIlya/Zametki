from colorama import Fore, Style


class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(note)

    @staticmethod
    def show_note(note):
        print(note)

    @staticmethod
    def show_empty_list_message():
        print('Cписок заметок пустой!')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print('Заметка с id: {} не найдена!'.format(note_id))

    @staticmethod
    def display_note_id_exist(note_id):
        print('Заметка с id: {} уже есть!'.format(note_id))

    @staticmethod
    def display_note_stored():
        print(Fore.GREEN + 'Заметка успешно добавлена!' + Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.GREEN + 'Заметка с id:{} обновлена успешно!'
              .format(note_id) + Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print(Fore.LIGHTRED_EX + 'Удаление заметки с id: {} выполнено!'.format(note_id) + Style.RESET_ALL)

    @staticmethod
    def display_all_notes_deletion():
        print('Все заметки удалены!')


def display_note_id_not_exist(search_id):
    return search_id
