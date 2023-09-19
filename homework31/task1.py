import json
from truck import Truck

def read_file (info):
    with open(info, 'r') as fp:
        trucks_data = json.load(fp)
        return [Truck(**truck) for truck in trucks_data]

# trucks = read_file('info.json')
# for truck in trucks:
#     print(truck)


trucks = input('Введите путь к файлу: ')

while True:
    
    if trucks is True:
        for truck in trucks:
            print(truck)
    else:
        print('нет файла')
        break