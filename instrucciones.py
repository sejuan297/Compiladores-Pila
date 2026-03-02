from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional

class OpCode(Enum):
    """Instrucciones del compilador."""
    
    # Manipulación de pila
    PUSH_CONST = auto()
    POP = auto()
    
    # Operaciones aritméticas
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    
    # Manejo de variables
    STORE = auto()
    LOAD = auto()
    
    # Control
    PRINT = auto()
    HALT = auto()

@dataclass(frozen=True)
class Instruccion:
    """Representa una instrucción de bytecode."""
    opcode: OpCode
    argumento: Optional[Any] = None

    def __str__(self) -> str:
        return f"{self.opcode.name}" + (f" {self.argumento}" if self.argumento is not None else "")
