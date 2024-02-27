from enum import Enum


class MachineState(Enum):
    WORKING = "Working"
    BROKEN = "Broken"
    IDLE = "Idle"
    REPAIRING = "Repairing"
    
class FactoryData:
    def __init__(self,log:str,state:MachineState):
        self.log = log
        self.state = state
    
class FactoryDataCollector:
    def __init__(self,needed_machines:int, idle_machines:int):
        self.__logs = []
        self.__needed_machines = needed_machines
        self.__idle_machines = idle_machines
        
    def add_log(self,data:FactoryData):
        self.__logs.append(data)
        
    def add_working_time(self,working_time:float):
        self.__working_time = working_time
    
    def get_logs(self):
        return self.__logs
    
    def get_working_time(self):
        return self.__working_time
    
    def get_needed_machines(self):
        return self.__needed_machines
    
    def get_idle_machines(self):
        return self.__idle_machines