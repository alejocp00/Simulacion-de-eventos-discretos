from scipy.stats import expon, norm

def get_working_time():
    # Utiliza una distribución exponencial para el tiempo de reparación (G(t))
    return expon.rvs()

def get_repair_time():
    # Utiliza una distribución normal para el tiempo de falla (F(t))
    return norm.rvs()

