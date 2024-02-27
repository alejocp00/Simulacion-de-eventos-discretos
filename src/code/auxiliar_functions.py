import random
from scipy.stats import expon, norm

def get_working_time():
    # Utiliza una distribución exponencial para el tiempo de reparación (G(t))
    return random.expovariate(1)

def get_repair_time():
    # Utiliza una distribución normal para el tiempo de falla (F(t))
    return random.normalvariate(1,0.2)

