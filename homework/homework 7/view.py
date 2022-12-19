def view_com():
    print('''Возможные команды:
    import - импортировать справочник
    print - вывести справочник в консоль
    add - добавить новую запись
    del - удалить запись (по фамилии)
    export - экспортировать справочник''')
    return input('Введите одну изкоманд: ')

def new_contact():
    contact = []
    contact.append(input('Введите фамилию: '))
    contact.append(input('Введите имя: '))
    contact.append(input('Введите телефон: '))
    contact.append(input('Введите описание: '))
    return contact

def del_contact():
    contact = input('Введите фамилию контакты который хотите удалить: ')
    return contact