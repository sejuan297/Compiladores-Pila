from typing import Generic, List, TypeVar

T = TypeVar('T')

class Pila(Generic[T]):
    """
    PILA - ESTRUCTURA FUNDAMENTAL EN COMPILADORES
    
    FUNCIÓN EN EL COMPILADOR:
    La pila es el corazón de las máquinas virtuales basadas en pila. Aquí se 
    almacenan temporalmente los operandos y los resultados intermedios durante
    la ejecución de instrucciones del compilador.
    
    IMPORTANCIA EN EL PROCESO DE COMPILACIÓN:
    - Permite evaluar expresiones complejas sin necesidad de registros explícitos
    - Facilita la generación de código intermedio (bytecode)
    - Es el modelo de ejecución usado por JVM, Python VM, .NET IL
    - Simplifica el diseño del compilador al estandarizar el manejo de operandos
    
    EJEMPLO: Para calcular (2 + 3) * 4:
    1. PUSH 2     -> [2]
    2. PUSH 3     -> [2, 3] 
    3. ADD        -> [5]  (2+3)
    4. PUSH 4     -> [5, 4]
    5. MUL        -> [20] (5*4)
    """
    
    def __init__(self) -> None:
        """Inicializa una pila vacía lista para ejecutar instrucciones."""
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """
        Apila un elemento en la cima.
        
        Uso en compilación: Coloca operandos para operaciones subsiguientes.
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """
        Desapila y retorna el elemento de la cima.
        
        Uso en compilación: Obtiene operandos para ejecutar operaciones.
        """
        if not self._items:
            raise IndexError("Pila vacía: no se puede hacer pop()")
        return self._items.pop()
    
    def peek(self) -> T:
        """
        Observa el elemento de la cima sin removerlo.
        
        Uso en compilación: Inspección del estado durante debugging.
        """
        if not self._items:
            raise IndexError("Pila vacía: no se puede hacer peek()")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Retorna el número de elementos en la pila."""
        return len(self._items)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Pila({self._items})"
