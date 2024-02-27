import random

from src.code.factory import Factory

# Todo: sacar el data collector a una clase
# Todo: Manejar la data

class Simulator:
    def __init__(self,i:int =0,n:int =0,s:int =0,random_values:bool = True):
        self.__iterations = i
        self.__n = n
        self.__s = s
        self.__random_values = random_values
        self.__results = []

        if self.__random_values:
            self.__n = random.randint(10,50)
            self.__s = random.randint(10,50)
            # self.__iterations = random.randint(1000,10000)
            self.__iterations = 10
            
    def run(self):
        for i in range(self.__iterations):
            factory = Factory(self.__n,self.__s)
            factory.start_factory()
            factory_time = factory.get_factory_time()
            factory_data = factory.get_data()
            self.__results.append((factory_time,factory_data))
            
    def get_results(self):
        return self.__results
    
    def show_results(self):
        for (factory_time,factory_data) in self.__results:
            print(f"Factory ran for {factory_time} seconds")
            print(factory_data)
            print("\n")