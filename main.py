from src.code.simulator import Simulator

def main():
    simulator = Simulator(n=10,s=10,i=10,random_values=False)
    simulator.run()
    simulator.show_results()
    
main()

# Todo: Permitir correr el programa con argumentos