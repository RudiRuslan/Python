from model import read_csv, find_worker, find_worker_by_title, find_worker_by_salary, \
                  add_worker, csv_export, delete_worker, update_worker_data, json_export
from view import show_menu as ui


def controller():
    position = -1
    while position != 9:
        position = ui()
        data = read_csv()
        match position:
            case 1:
                find_worker(data)
            case 2:
                find_worker_by_title(data)
            case 3:
                find_worker_by_salary(data)
            case 4:
                add_worker(data)
            case 5:
                delete_worker(data)
            case 6:
                update_worker_data(data)
            case 7:
                json_export(data)
            case 8:
                csv_export(data)
    else:
        print("\t========== Конец работы ==========")
