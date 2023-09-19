from states import State
from random import randint

class InRepairState(State):
    name = "repair"

    def change_driver(self, driver):
        self._truck.driver = driver
        print(f' Водитель грузовика {self._truck.name} поменялся {self._truck.driver}')
    
    def start_run(self):
        if randint (1,2) == 1:
     
            self._truck.change_state('run')
            print(f'Грузовик {self._truck.name} отправился в путь')
        else:
            self._truck.change_state('base')
            print(f'Грузовик {self._truck.name} отправился на базу')

    def start_repair(self):
        print(f'Грузовик {self._truck.name} уже в ремонте')