from dataclasses import dataclass

@dataclass
class Chave:
    n: int
    e: int
    d: int | None = None      # None numa chave "só verificação"
    p: int | None = None      # guardados para CRT e para o Bellcore
    q: int | None = None

def keygen(bits: int = 1024, e: int = 65537) -> Chave
def chave_publica(chave: Chave) -> Chave          # cópia sem d, p, q

def fdh(msg: bytes, n: int) -> int
def h(msg: bytes, n: int, modo: str = 'fdh') -> int        # modo: 'livro' | 'fdh'

def sign(msg: bytes, chave: Chave, modo: str = 'fdh') -> int
def sign_crt(msg: bytes, chave: Chave, modo: str = 'fdh', falha: bool = False) -> int
def sign_raw(x: int, chave: Chave) -> int         # xᵈ mod n, sem hash — é o que o oráculo expõe

def verify(msg: bytes, s: int, n: int, e: int, modo: str = 'fdh') -> bool

class Esquema:
    def __init__(self, modo: str = 'fdh'): ...
    def h(self, msg: bytes, n: int) -> int
    def assinar(self, msg: bytes, chave: Chave) -> int
    def verificar(self, msg: bytes, s: int, n: int, e: int) -> bool