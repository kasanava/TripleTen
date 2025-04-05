import math

def is_prime(n):
    """Devuelve True si n es primo, False en caso contrario"""
    # Un número es primo si no es divisible por ningún número entre 2 y su raíz cuadrada
    # Si n es menor o igual a 1, no es primo
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():

    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
