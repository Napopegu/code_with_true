from states import State

class InRunState(State):
    name = 'run'

    def change_driver(self, driver):
        print(f'Нельзя менять водителя грузовик {self._truck.name}в пути')
    
    def start_run(self):
        print(f'Грузовик {self._truck.name} и так в пути')

    def start_repair(self):
        self._truck.change_state('repair')
        print(f'Грузовик {self._truck.name} отправился на ремонт')