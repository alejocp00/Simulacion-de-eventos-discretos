import time
from src.code.auxiliar_functions import  get_working_time

class Machine:
    def __init__(self,id,work_time=0):
        self.__id = id
        self.__work_time = work_time if not work_time == 0 else get_working_time()
        self.__start_time = 0
        
    def get_id(self):
        return self.__id
    
    def get_work_time(self) -> float:
        return self.__work_time
    
    def get_start_time(self) -> float:
        return self.__start_time
    
    def start_working(self):
        self.__start_time = time.time()
        
    def repair(self):
        self.__work_time = get_working_time()
        
    def __lt__(self, other):
        if isinstance(other, Machine):
            return self.__work_time < other.__work_time
        
    def __eq__(self, other):
        if isinstance(other, Machine):
            return self.__work_time == other.__work_time
        return False
    
    
    