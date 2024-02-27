from src.code.factory import Factory
import time

def main():
    n = 10
    s = 10
    factory = Factory(n,s)
    start = time.time()
    factory.start_factory()
    end = time.time()
    print(f"Factory ran for {end-start} seconds")
    
main()