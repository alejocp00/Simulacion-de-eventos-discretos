import heapq
from platform import machine
from threading import Thread
import time
from queue import Queue

from src.code.factory_data_collector import MachineData, FactoryDataCollector, MachineState
from src.code.machines import Machine


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
        
        self.__perform_work_routine()
        
        self.__factory_crashed()

    def __run_all_machines(self):
        for machine in self.__working_machines:
            machine.start_working()
            self.__data_collector.add_log(MachineData(machine,MachineState.WORKING))
            
            
    def __populate_factory(self):
        self.__working_machines : list[Machine] = []  
        self.__idle_machines = Queue()
        for i in range(self.s):
            machine = Machine(self.n+i)
            self.__idle_machines.put(machine)
        
        heapq.heapify(self.__working_machines)
        
        for i in range(self.n):
            machine = Machine(i)
            heapq.heappush(self.__working_machines, machine)
            
    def __repair_machine(self):
        while not self.__crashed:
            # Check if there are broken machines to repair
            if not self.__broken_machines.empty():
                
                # Get the broken machine and repair it
                machine = self.__broken_machines.get()
                
                # Update the logs
                self.__data_collector.add_log(MachineData(machine,MachineState.REPAIRING))
                
                # Simulate the repair time
                repair_time = machine.get_repair_time()
                time.sleep(repair_time)
                if self.__crashed:
                    break
                machine.repair()
                
                # Put the machine to idle state and update logs
                self.__idle_machines.put(machine)
                self.__data_collector.add_log(MachineData(machine,MachineState.IDLE))
                
    def __perform_work_routine(self):
        machine = heapq.heappop(self.__working_machines)
        
        while True:
            
            # Check if the machine is broken
            if machine.get_start_time() + machine.get_work_time() < time.time():
                
                # Update logs
                self.__data_collector.add_log(MachineData(machine,MachineState.BROKEN))
                
                # Put the machine to broken state
                self.__broken_machines.put(machine)
                
                # Check if there are available machines to replace the broken one
                if self.__idle_machines.empty():
                    break
                
                # Replace the broken machine
                self.__remplace_machine()
                
                # Get the next machine
                machine = heapq.heappop(self.__working_machines)
            
                
    def __remplace_machine(self):
        new_machine = self.__idle_machines.get()
        new_machine.start_working()
        self.__data_collector.add_log(MachineData(new_machine,MachineState.WORKING))
        heapq.heappush(self.__working_machines, new_machine)

        
    def __factory_crashed(self):
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