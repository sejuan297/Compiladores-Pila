from typing import Dict, List, Any
from pila import Pila
from instrucciones import Instruccion, OpCode

class MaquinaVirtual:
    """
    MÁQUINA VIRTUAL BASADA EN PILA
    
    FUNCIÓN EN EL COMPILADOR:
    Es el motor de ejecución que corre el bytecode generado por el compilador.
    Implementa el modelo de ejecución basado en pila para interpretar las
    instrucciones compiladas.
    
    IMPORTANCIA EN EL PROCESO DE COMPILACIÓN:
    - Separa completamente el análisis del código fuente de su ejecución
    - Permite que el mismo bytecode corra en diferentes plataformas
    - Facilita la optimización del código en tiempo de ejecución
    - Es el componente que da vida al código compilado
    
    ARQUITECTURA:
    - stack: Pila donde operan las instrucciones
    - memoria: Almacena variables (entorno de ejecución)
    - ip: Instruction Pointer (siguiente instrucción a ejecutar)
    """
    
    def __init__(self) -> None:
        """Inicializa la máquina virtual con pila, memoria y contador de programa."""
        self.stack: Pila[Any] = Pila()
        self.memoria: Dict[str, Any] = {}
        self.ip: int = 0  # Instruction Pointer
    
    def ejecutar(self, programa: List[Instruccion]) -> None:
        """
        Ejecuta un programa completo (lista de instrucciones).
        
        Proceso: Recorre secuencialmente las instrucciones, ejecutando
        cada una según su OpCode y modificando el estado de la máquina.
        """
        self.ip = 0
        self.stack = Pila()  # Reiniciar pila
        self.memoria.clear() # Reiniciar memoria
        
        while self.ip < len(programa):
            instruccion_actual = programa[self.ip]
            self._ejecutar_instruccion(instruccion_actual)
            self.ip += 1
    
    def _ejecutar_instruccion(self, instruccion: Instruccion) -> None:
        """
        Ejecuta una instrucción individual según su OpCode.
        
        Cada operación modifica la pila, memoria o el flujo de ejecución
        según la semántica de las máquinas virtuales basadas en pila.
        """
        op = instruccion.opcode
        arg = instruccion.argumento
        
        if op == OpCode.PUSH_CONST:
            # Apilar constante en la pila
            self.stack.push(arg)
            
        elif op == OpCode.POP:
            # Desapilar (descartar valor)
            self.stack.pop()
            
        elif op == OpCode.ADD:
            # Sumar: a + b (consume 2, produce 1)
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.push(a + b)
            
        elif op == OpCode.SUB:
            # Restar: a - b (consume 2, produce 1)
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.push(a - b)
            
        elif op == OpCode.MUL:
            # Multiplicar: a * b (consume 2, produce 1)
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.push(a * b)
            
        elif op == OpCode.DIV:
            # Dividir: a / b (consume 2, produce 1)
            b = self.stack.pop()
            a = self.stack.pop()
            if b == 0:
                raise ZeroDivisionError("División por cero")
            self.stack.push(a / b)
            
        elif op == OpCode.STORE:
            # Almacenar valor en variable
            nombre_var = str(arg)
            valor = self.stack.pop()
            self.memoria[nombre_var] = valor
            
        elif op == OpCode.LOAD:
            # Cargar valor de variable a la pila
            nombre_var = str(arg)
            if nombre_var not in self.memoria:
                raise NameError(f"Variable '{nombre_var}' no definida")
            self.stack.push(self.memoria[nombre_var])
            
        elif op == OpCode.PRINT:
            # Imprimir valor en la cima de la pila
            valor = self.stack.pop()
            print(f"OUTPUT: {valor}")
            
        elif op == OpCode.HALT:
            # Detener ejecución
            return
            
        else:
            raise ValueError(f"OpCode no implementado: {op}")
    
    def obtener_estado(self) -> Dict[str, Any]:
        """
        Retorna el estado actual de la máquina para debugging.
        """
        return {
            "pila": list(self.stack._items),
            "memoria": self.memoria.copy(),
            "instruction_pointer": self.ip
        }
