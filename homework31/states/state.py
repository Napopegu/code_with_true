from abc import ABC, abstractmethod

class State(ABC):
    name = None
    def __init__(self):
        self._truck = None

    def set_truck(self, truck):
        self._truck = truck
    
    @abstractmethod
    def change_driver(self, driver):
        pass
    
    @abstractmethod
    def start_run(self):
        pass

    @abstractmethod
    def start_repair(self):
        pass