import random
from scipy.stats import expon, norm

var_lambd = 1
var_mu = 1
var_sigma = 0.5

def get_working_time(lambd:float = var_lambd):
    # Utiliza una distribución exponencial para el tiempo de reparación (G(t))
    return random.expovariate(lambd)

def get_repair_time(mu:float = var_mu, sigma:float = var_sigma):
    # Utiliza una distribución normal para el tiempo de falla (F(t))
    return random.normalvariate(mu,sigma)