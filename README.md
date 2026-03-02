# Compilador de Pila - Proyecto de Estructuras de Datos

## Descripción
Este proyecto implementa un compilador simple basado en pila para la materia de Estructuras de Datos. El sistema puede compilar expresiones matemáticas básicas y ejecutarlas en una máquina virtual.

## Componentes

- `pila.py` - Implementación de la estructura de datos pila
- `instrucciones.py` - Códigos de operación para la máquina virtual
- `maquina_virtual.py` - Máquina virtual que ejecuta el bytecode
- `ejemplo.py` - Ejemplos de uso del compilador

## Cómo ejecutar

```bash
python ejemplo.py
```

## Ejemplos

El compilador puede procesar expresiones como:
- `(10 + 5) * (8 - 3) = 75`
- Variables: `x = 7; y = 3; z = x * y + 10`

## Estructura del compilador

1. **Análisis**: Convierte expresiones a notación postfija
2. **Generación**: Crea bytecode para la máquina virtual
3. **Ejecución**: La máquina virtual procesa el bytecode usando una pila

## Referencias
- Compiladores: Principios, técnicas y herramientas - Aho et al.
- Apuntes de clase de Estructuras de Datos
