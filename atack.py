class ServicoDeAssinatura:
    def __init__(self, chave: Chave, esquema: Esquema)
    def assinar(self, x: int) -> int     # expõe xᵈ mod n — vulnerável em modo 'livro'

def ataque_cego(payload: bytes, oraculo: Callable[[int], int], e: int, n: int, esquema: Esquema) -> int
def cenario(modo: str, bits: int = 1024) -> tuple[bool, int]   # ataque fim a fim contra a cadeia real


