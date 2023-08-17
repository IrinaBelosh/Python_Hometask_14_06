# вводим функцию выбора режима работы со справочником
def choose_mode():
    mode = input('Введите режим работы (запись, поиск, удаление или изменение): ')
    if mode == 'запись':
        person = person_data()
    elif mode == 'поиск':
        person = find_data()
    elif mode == 'удаление':
        person = input('Введите фамилию: ')
    elif mode == 'изменение':
        person = input('Введите фамилию: ')
    else:
        print('Такой режим не предусмотрен.')
        choose_mode()
    return person, mode

def person_data(): # функция запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return  surname, name, patronymic, phone_number

def fill_notebook(person): # функция записывает данные в записную книжку
    with open('sem8_example.txt', 'a', encoding='utf-8') as file:
        for element in person:
            file.write(element + '\n')
        file.write('\n')

def find_data(): # функция запрашивает данные для поиска
    surname = input('Введите фамилию: ')
    return surname

def find_person(surname): # функция поиска данных по фамилии
    with open('sem8_example.txt', 'r', encoding='utf-8') as file:
        dat = file.read().splitlines()
        for i in range(len(dat)):
            if dat[i] == surname:
                print(f'Фамилия: {dat[i]}')
                print(f'Имя: {dat[i+1]}')
                print(f'Отчество: {dat[i+2]}')
                print(f'Телефон: {dat[i+3]}')

def delete_data(person):
    with open('sem8_example.txt', 'r', encoding='utf-8') as file:
        dat = file.read().splitlines()
    for i in range(len(dat)):
        if dat[i] == person:
            del dat[i:i+5]
            break
    with open('sem8_example.txt', 'w', encoding='utf-8') as file:
        for el in dat:
            file.write(el + '\n')

def change_data(person):
    with open('sem8_example.txt', 'r', encoding='utf-8') as file:
        dat = file.read().splitlines()
        for i in range(len(dat)):
            if dat[i] == person:
                print(f'Фамилия: {dat[i]}')
                print(f'Имя: {dat[i+1]}')
                print(f'Отчество: {dat[i+2]}')
                print(f'Телефон: {dat[i+3]}')
                dat[i] = input('Введите новую фамилию: ')
                dat[i+1] = input('Введите новое имя: ')
                dat[i+2] = input('Введите новое отчество: ')
                dat[i+3] = input('Введите новый телефон: ')
    with open('sem8_example.txt', 'w', encoding='utf-8') as file:
        for el in dat:
            file.write(el + '\n')   











        
