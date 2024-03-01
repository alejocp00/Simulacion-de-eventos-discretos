import random
from src.code.factory_data_collector import FactoryDataCollector
from src.code.factory import Factory
import src.code.auxiliar_functions as aux

# Todo: sacar el data collector a una clase
# Todo: Manejar la data

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

    def show_results(self):
        for factory_data in self.__results:
            print(f"Factory ran for {factory_data.get_working_time()} seconds")
            print(factory_data.get_logs())
            print("\n")
