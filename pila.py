from typing import Generic, List, TypeVar

T = TypeVar('T')

class Pila(Generic[T]):
    """
    Pila LIFO para el compilador.
    """
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Apila un elemento."""
        self._items.append(item)
    
    def pop(self) -> T:
        """Desapila y retorna el elemento de la cima."""
        if not self._items:
            raise IndexError("Pila vacía")
        return self._items.pop()
    
    def peek(self) -> T:
        """Observa el elemento de la cima sin desapilarlo."""
        if not self._items:
            raise IndexError("Pila vacía")
        return self._items[-1]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Pila({self._items})"
