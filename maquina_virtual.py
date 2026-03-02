from typing import Dict, List, Any
from pila import Pila
from instrucciones import Instruccion, OpCode

class MaquinaVirtual:
    """Máquina virtual basada en pila."""
    
    def __init__(self) -> None:
        self.pila: Pila[Any] = Pila()
        self.memoria: Dict[str, Any] = {}
        self.ip: int = 0

    def ejecutar(self, programa: List[Instruccion]) -> None:
        self.ip = 0
        while self.ip < len(programa):
            instr = programa[self.ip]
            op = instr.opcode

            if op == OpCode.PUSH_CONST:
                self.pila.push(instr.argumento)
            elif op == OpCode.ADD:
                b = self.pila.pop()
                a = self.pila.pop()
                self.pila.push(a + b)
            elif op == OpCode.SUB:
                b = self.pila.pop()
                a = self.pila.pop()
                self.pila.push(a - b)
            elif op == OpCode.MUL:
                b = self.pila.pop()
                a = self.pila.pop()
                self.pila.push(a * b)
            elif op == OpCode.DIV:
                b = self.pila.pop()
                a = self.pila.pop()
                self.pila.push(a / b)
            elif op == OpCode.STORE:
                nombre = str(instr.argumento)
                valor = self.pila.pop()
                self.memoria[nombre] = valor
            elif op == OpCode.LOAD:
                nombre = str(instr.argumento)
                if nombre not in self.memoria:
                    raise NameError(f"Variable '{nombre}' no definida")
                self.pila.push(self.memoria[nombre])
            elif op == OpCode.PRINT:
                valor = self.pila.pop()
                print(valor)
            elif op == OpCode.HALT:
                return
            else:
                raise ValueError(f"OpCode no soportado: {op}")

            self.ip += 1
