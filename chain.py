def merkle_root(ids: list[bytes]) -> bytes
def endereco_de(n: int, e: int) -> bytes          # SHA-256(n‖e), truncado

@dataclass
class Tx:
    de_n: int
    de_e: int
    para: bytes
    valor: int
    contador: int
    assinatura: int | None = None
    def payload(self) -> bytes                     # bytes que são assinados/verificados
    def id(self) -> bytes                           # hash da tx, folha do Merkle
    def assinar(self, chave: Chave, esquema: Esquema) -> None
    def verificar(self, esquema: Esquema) -> bool

class Carteira:
    def __init__(self, bits: int = 1024)
    @property
    def endereco(self) -> bytes
    def nova_tx(self, para: bytes, valor: int, contador: int) -> Tx
    def assinar_tx(self, tx: Tx, esquema: Esquema) -> None

@dataclass
class Block:
    indice: int
    prev: bytes
    timestamp: float
    alvo: int
    txs: list[Tx]
    nonce: int = 0
    def merkle(self) -> bytes
    def hash(self) -> bytes
    def minerar(self) -> None                       # incrementa nonce até hash() < alvo

class Estado:
    def __init__(self)
    def saldo(self, endereco: bytes) -> int
    def contador(self, endereco: bytes) -> int
    def aplicar(self, tx: Tx, esquema: Esquema) -> None    # ValueError se inválida

class Blockchain:
    def __init__(self, esquema: Esquema, dificuldade_bits: int = 16)
    def genesis(self) -> Block
    def receber(self, tx: Tx) -> bool               # entra na mempool se válida
    def minerar(self, recompensa_para: bytes) -> Block
    def saldo(self, endereco: bytes) -> int
    def validar(self) -> bool

def validar_cadeia(blocos: list[Block], esquema: Esquema) -> bool   # usada nos testes