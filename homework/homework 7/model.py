import csv
data_list = []

def init(data):
    global data_list 
    data_list = list(data)
    
def data_reader():
    full_contacts = []
    with open('file.txt', 'r', encoding='utf-8') as data:
        count = 0
        contact = []
        while True:
            x = data.readline().replace('\n', '')
            if x == '':
                count += 1
                if count == 2:
                    return full_contacts
                full_contacts.append(contact)
                contact = []
            else:
                count = 0
                contact.append(x)
            
def data_add(data):
    data_list.append(data)

def data_del(data):
    for i in data_list:
        if i[0] == data:
            data_list.remove(i)

def data_print():
    for i in data_list:
        for j in i:
            print(j)
        print('')

def data_export():
    data = open('new_file.csv', 'w', encoding='utf-8')
    file_writer = csv.writer(data, delimiter=',', lineterminator='\r')
    file_writer.writerow(["Имя", "Фамилия", "Телефон", "Описание"])
    for i in data_list:
        file_writer.writerow(i) 
    data.close()