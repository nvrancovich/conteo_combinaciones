def formula(n,r):
    nr = n - r
    n_factorial = 1
    r_factorial = 1
    nr_factorial = 1
    if n > 0:
        for i in range(1, n + 1):
            n_factorial = n_factorial*i
    if r > 0:
        for i in range(1, r + 1):
            r_factorial = r_factorial*i
    if nr > 0:
        for i in range(1, (nr) + 1):
            nr_factorial = nr_factorial*i
    return n_factorial / (r_factorial * nr_factorial)
    

def run():
    n = int(input('Inserte la cantidad de la cantidad de objetos (n)'))
    r = int(input('Inserte la amplitud de las agrupaciones (r)'))
    c = int(formula(n,r))
    print('La cantidad de posible de agrupaciones es igual a', c)

if __name__ == '__main__':
    run()