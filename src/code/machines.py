import time
from src.code.auxiliar_functions import  get_repair_time, get_working_time

class Machine:
    def __init__(self,id,work_time=-1,repair_time=-1):
        self.__id = id
        self.__work_time = work_time if not work_time == -1 else get_working_time()
        self.__repair_time = repair_time if not repair_time == -1 else get_repair_time()
        self.__start_time = 0
        
    def get_id(self):
        return self.__id
    
    def get_work_time(self) -> float:
        return abs(self.__work_time)
    
    def get_repair_time(self) -> float:
        return abs(self.__repair_time)
    
    def get_start_time(self) -> float:
        return abs(self.__start_time)
    
    def start_working(self):
        self.__start_time = time.time()
        
    def repair(self):
        self.__work_time = get_working_time()
        self.__repair_time = get_repair_time()
        
    def __lt__(self, other):
        if isinstance(other, Machine):
            return self.__work_time < other.__work_time
        
    def __eq__(self, other):
        if isinstance(other, Machine):
            return self.__work_time == other.__work_time
        return False
    
    
    