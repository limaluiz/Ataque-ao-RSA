def mdc(a: int, b: int) -> int: # Funcionando
    '''
    Retorna o mdc entre a e b
    '''
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    
    menor = min(a, b)
    result = 1
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0:
            result = i  # guardando o maior divisor comum
    return result


def euclides_estendido(a: int, b: int) -> tuple[int, int, int]: 
    '''
    Retorna a tupla (mdc(a, b), x, y) onde a*x + b*y = g.
    '''
    if b == 0: # Condiçaõ de Parada
        return a, 1, 0
    g, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y



def inverso_mod(a: int, n: int) -> int: # a⁻¹ mod n; ValueError se mdc(a,n) != 1
    if mdc(a, n) != 1:
        raise ValueError

    return euclides_estendido(a, n)[1] # Devido ao Teorema de Bezout-Barchet


def crt(residuos: list[int], modulos: list[int]) -> int: # Teorema Chinês dos Restos
    pass


def miller_rabin(n: int, k: int = 40) -> bool:
    pass


def gerar_primo(bits: int) -> int: # Mais básico de todos, multiplica todos os primos e até a posição n e soma 1.
    pass


def ordem(a: int, n: int) -> int: # ordem de a em ℤₙ* — experimento 1
    pass

def unidades(n: int) -> list[int]: # elementos de ℤₙ* — experimento 1
    pass