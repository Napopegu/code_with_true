from states import InRunState, InBaseState, InRepairState


class Truck:
    def __init__(self,id,name,driver,state_name):
        self.id = id
        self.name = name
        self.driver = driver
        self.state = None
        self.change_state(state_name)

    def change_state(self,state_name):
        match state_name:
            case InRunState.name:
                self.state = InRunState()
            case InBaseState.name:
                self.state = InBaseState()
            case InRepairState.name:
                self.state = InRepairState()

        self.state.set_truck(self)

    def change_driver(self,driver):
        self.state.change_driver(driver)
    
    def start_run(self):
        self.state.start_run()

    def start_repair(self):
        self.state.start_repair()
    
    def __str__(self) -> str:
        return f'{self.id:<5}|{self.name:>15}| {self.driver:>15}| {self.state.name:>15}'