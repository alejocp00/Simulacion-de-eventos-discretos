from enum import Enum
import re

from src.code.machines import Machine


class MachineState(Enum):
    WORKING = "Working"
    BROKEN = "Broken"
    IDLE = "Idle"
    REPAIRING = "Repairing"
    
class FactoryData:
    def __init__(self,machine:Machine,state:MachineState):
        self.__machine_work_time = machine.get_work_time()
        self.__machine_repair_time = machine.get_repair_time()
        self.__machine_id = machine.get_id()
        
        self.__state = state
        
        
    def get_machine_id(self):
        return self.__machine_id
    
    def get_state(self):
        return self.__state
    
    def get_machine_work_time(self):
        return self.__machine_work_time
    
    def get_machine_repair_time(self):
        return self.__machine_repair_time
    
        
    def __str__(self) -> str:
        if self.__state == MachineState.WORKING:
            return f"Machine {self.__machine_id} start working"
        if self.__state == MachineState.BROKEN:
            return f"Machine {self.__machine_id} broke. Work for {self.__machine_work_time} seconds"
        if self.__state == MachineState.IDLE:
            return f"Machine {self.__machine_id} already repaired. Repair time: {self.__machine_repair_time} seconds"
        if self.__state == MachineState.REPAIRING:
            return f"Machine {self.__machine_id} is repairing"
        return "Wrong log format"
    
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
    
    def __str__(self) -> str:
        
        logs = "\n".join([str(log) for log in self.__logs])
        return f"Logs:\n{logs}\nWorking time: {self.__working_time}\nNeeded machines: {self.__needed_machines}\nIdle machines: {self.__idle_machines}"