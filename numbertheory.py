def mdc(a: int, b: int) -> int
def euclides_estendido(a: int, b: int) -> tuple[int, int, int]   # (g, x, y): a*x + b*y = g
def inverso_mod(a: int, n: int) -> int                           # a⁻¹ mod n; ValueError se mdc(a,n) != 1
def crt(residuos: list[int], modulos: list[int]) -> int          # Teorema Chinês dos Restos
def miller_rabin(n: int, k: int = 40) -> bool
def gerar_primo(bits: int) -> int
def ordem(a: int, n: int) -> int                                 # ordem de a em ℤₙ* — experimento 1
def unidades(n: int) -> list[int]                                # elementos de ℤₙ* — experimento 1