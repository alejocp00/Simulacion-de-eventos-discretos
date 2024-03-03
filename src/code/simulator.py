import random
from src.code.factory_data_collector import FactoryDataCollector
from src.code.factory import Factory
import src.code.auxiliar_functions as aux
import numpy as np


ITERATIONS = 100
N = 10
S = 10
LAMBD = 1
MU = 1
SIGMA = 0.5
RANDOM_VALUES = False


class Simulator:
    def __init__(
        self,
        iter: int,
        n: int,
        s: int,
        lambd: float,
        mu: float,
        sigma: float,
        random_values: bool,
    ):
        self.__iterations = iter
        self.__n = n
        self.__s = s
        self.__lambd = lambd
        self.__mu = mu
        self.__sigma = sigma
        aux.var_lambd = lambd
        aux.var_mu = mu
        aux.var_sigma = sigma

        self.__random_values = random_values
        self.__results: list[FactoryDataCollector] = []

        if self.__random_values:
            self.__n = random.randint(10, 50)
            self.__s = random.randint(10, 50)
            self.__iterations = random.randint(100,1000)
            self.__iterations = 10

    def run(self):
        for i in range(self.__iterations):
            factory = Factory(self.__n, self.__s)
            factory.start_factory()
            factory_data = factory.get_data()
            self.__results.append(factory_data)

    def get_results(self):
        return self.__results

    def get_results_as_text(self):
        result= ""
        for factory_data in self.__results:
            result +=f"Factory ran for {factory_data.get_working_time()} seconds"
            result += "\n"
            for log in factory_data.get_logs():
                result += "\t"
                result += str(log)
                result += "\n"
            result += "\n"
            
        result += f"Mean working time for given parameters: {self.get_mean_working_time()}"
            
        return result
    
    def get_iterations(self):
        return self.__iterations
    
    def get_n(self):
        return self.__n
    
    def get_s(self):
        return self.__s
    
    def get_lambd(self):
        return self.__lambd
    
    def get_mu(self):
        return self.__mu
    
    def get_sigma(self):
        return self.__sigma

    def get_mean_working_time(self):
        return np.mean([factory_data.get_working_time() for factory_data in self.__results])