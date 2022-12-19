import model
import view

def start():
    com = view.view_com()
    if com == 'import':
        model.init(model.data_reader())
    elif com == 'print':
        model.data_print()
    elif com == 'add':
        data = view.new_contact()
        model.data_add(data)
    elif com == 'del':
        data = view.del_contact()
        model.data_del(data)
    elif com == 'export':
        model.data_export()
        return 1
    return 0