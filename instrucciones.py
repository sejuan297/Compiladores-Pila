from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional

class OpCode(Enum):
    """
    CONJUNTO DE INSTRUCCIONES DEL COMPILADOR
    
    FUNCIÓN EN EL COMPILADOR:
    Define el lenguaje máquina que el compilador genera. Cada OpCode
    representa una operación fundamental que la máquina virtual puede ejecutar.
    
    IMPORTANCIA EN EL PROCESO DE COMPILACIÓN:
    - Es el resultado final del proceso de compilación (bytecode)
    - Permite separar el análisis del código fuente de su ejecución
    - Facilita la optimización y portabilidad del código compilado
    - Es el puente entre el lenguaje de alto nivel y la máquina virtual
    """
    
    # MANIPULACIÓN DE PILA
    PUSH_CONST = auto()  # Apilar constante: PUSH_CONST 5
    POP = auto()         # Desapilar: POP
    
    # OPERACIONES ARITMÉTICAS
    ADD = auto()         # Sumar: a + b
    SUB = auto()         # Restar: a - b  
    MUL = auto()         # Multiplicar: a * b
    DIV = auto()         # Dividir: a / b
    
    # MANEJO DE VARIABLES
    STORE = auto()       # Almacenar en variable: STORE "x"
    LOAD = auto()        # Cargar variable: LOAD "x"
    
    # CONTROL DE FLUJO
    PRINT = auto()       # Imprimir valor en cima
    HALT = auto()        # Detener ejecución

@dataclass(frozen=True)
class Instruccion:
    """
    INSTRUCCIÓN - UNIDAD BÁSICA DEL BYTECODE
    
    FUNCIÓN EN EL COMPILADOR:
    Representa una operación atómica que la máquina virtual puede ejecutar.
    Es la unidad mínima de código generado por el compilador.
    
    IMPORTANCIA EN EL PROCESO DE COMPILACIÓN:
    - Permite representar programas como secuencias de operaciones simples
    - Facilita la optimización del código intermedio
    - Es el formato que la máquina virtual entiende y ejecuta
    - Permite análisis y transformación del código compilado
    
    EJEMPLO: Instruccion(OpCode.PUSH_CONST, 42) representa "apilar el valor 42"
    """
    opcode: OpCode
    argumento: Optional[Any] = None
    
    def __str__(self) -> str:
        if self.argumento is not None:
            return f"{self.opcode.name} {self.argumento}"
        return self.opcode.name
