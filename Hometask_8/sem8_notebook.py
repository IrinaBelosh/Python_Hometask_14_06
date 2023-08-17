from sem8_functions import *
def notebook():
    person, mode = choose_mode()
    if mode == 'запись':
        fill_notebook(person)
    elif mode == 'поиск':
        find_person(person)
    elif mode == 'удаление':
        delete_data(person)
    elif mode == 'изменение':
        change_data(person)




        