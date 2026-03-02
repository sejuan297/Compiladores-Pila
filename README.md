# Compilador de Pila

Un compilador educativo basado en pila que permite al usuario ingresar expresiones matemáticas y las compila a bytecode para ejecución en una máquina virtual.

## Características

- Ingresa tus propias expresiones matemáticas en tiempo real
- Convierte expresiones infijas a notación postfija (RPN)
- Genera bytecode ejecutable para máquina virtual de pila
- Operaciones aritméticas (+, -, *, /) y paréntesis
- Muestra el bytecode generado paso a paso

## Uso

```bash
cd NuevoCompiladorPila
python ejemplo.py
```

## Comandos

- Expresiones matemáticas: `2 + 3`, `(10 + 5) * (8 - 3)`
- ayuda: Muestra ejemplos de uso
- demo: Ejecuta demostración predefinida
- salir: Termina el programa

## Arquitectura

- `pila.py`: Estructura de datos LIFO
- `instrucciones.py`: OpCodes y definición de instrucciones
- `maquina_virtual.py`: Motor de ejecución de bytecode
- `ejemplo.py`: Compilador interactivo principal

## Licencia

Proyecto educativo de código abierto.
