from states import State

class InBaseState(State):
    name = 'base'

    
    def change_driver(self, driver):
        self._truck.driver = driver
        print(f' Водитель грузовика {self._truck.name} поменялся {self._truck.driver}')
    
    def start_run(self):
        self._truck.change_state('run')
        print(f'Грузовик {self._truck.name} отправился в путь')

    def start_repair(self):
        self._truck.change_state('repair')
        print(f'Грузовик {self._truck.name} отправился на ремонт')