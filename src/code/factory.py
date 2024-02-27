import heapq
from platform import machine
from threading import Thread
import time
from queue import Queue

from src.code.factory_data_collector import FactoryData, FactoryDataCollector, MachineState
from src.code.machines import Machine
from src.code.auxiliar_functions import get_repair_time

# Todo: cambiar a que el heap sólo reciba máquinas

class Factory:
    def __init__(self, n:int, s:int):
        self.n = n
        self.s = s
        self.__populate_factory()
        self.__broken_machines = Queue()
        self.__crashed = False
        self.__start_time = 0
        self.__working_time = 0
        self.__data_collector = FactoryDataCollector(n,s)
        
    def start_factory(self):
        self.__repair_thread = Thread(target=self.__repair_machine)
        self.__repair_thread.start()
        
        self.__run_all_machines()
        
        self.__start_time = time.time()
        
        self.__check_machines_state()
        
        self.__factory_crashed()

    def __run_all_machines(self):
        for (_,machine) in self.__working_machines:
            machine.start_working()
            self.__data_collector.add_log(FactoryData(f"Machine {machine.get_id()} started working",MachineState.WORKING))
            
            
    def __populate_factory(self):
        self.__working_machines : list[tuple[float,Machine]] = []  
        self.__idle_machines = Queue()
        for i in range(self.s):
            machine = Machine(self.n+i)
            self.__idle_machines.put(machine)
        
        heapq.heapify(self.__working_machines)
        
        for i in range(self.n):
            machine = Machine(i)
            heapq.heappush(self.__working_machines, (machine.get_work_time(), machine))
            
    def __repair_machine(self):
        while not self.__crashed:
            if not self.__broken_machines.empty():
                machine = self.__broken_machines.get()
                self.__data_collector.add_log(FactoryData(f"Machine {machine.get_id()} started repairing",MachineState.REPAIRING))
                repair_time=get_repair_time()
                time.sleep(repair_time)
                self.__idle_machines.put(machine)
                self.__data_collector.add_log(FactoryData(f"Machine {machine.get_id()} finished repairing: {repair_time}",MachineState.IDLE))
                
    def __check_machines_state(self):
        _,machine = heapq.heappop(self.__working_machines)
        while True:
            if machine.get_start_time() + machine.get_work_time() < time.time():
                
                self.__data_collector.add_log(FactoryData(f"Machine {machine.get_id()} broke: {machine.get_work_time()}",MachineState.BROKEN))
                self.__broken_machines.put(machine)
                
                # Check if there are available machines to replace the broken one
                if self.__idle_machines.empty():
                    break
                
                self.__swap_machine(machine)
                
                _,machine = heapq.heappop(self.__working_machines)
            
                
    def __swap_machine(self, machine):
        new_machine = self.__idle_machines.get()
        new_machine.start_working()
        self.__data_collector.add_log(FactoryData(f"Machine {new_machine.get_id()} started working",MachineState.WORKING))
        heapq.heappush(self.__working_machines, (new_machine.get_work_time(), new_machine))

        
    def __factory_crashed(self):
        print("The factory has crashed")
        self.__crashed = True
        self.__repair_thread.join()
        self.__working_time = time.time() - self.__start_time
        self.__data_collector.add_working_time(self.get_factory_time())
        
    def get_factory_time(self):
        if self.__crashed:
            return self.__working_time
        return time.time() - self.__start_time
    
    def get_data(self):
        return self.__data_collector