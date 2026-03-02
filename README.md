
# COMPILADOR DE PILA - PROYECTO EDUCATIVO

## DESCRIPCIÓN DEL PROYECTO

Este proyecto implementa un **compilador sencillo basado en pila** que demuestra los conceptos fundamentales del proceso de compilación. El sistema transforma expresiones matemáticas simples en bytecode que una máquina virtual puede ejecutar.

## OBJETIVOS DE APRENDIZAJE

- Comprender cómo funcionan las máquinas virtuales basadas en pila
- Entender el proceso de compilación: código fuente → bytecode → ejecución
- Aprender la importancia de la pila en la evaluación de expresiones
- Conocer la arquitectura de compiladores reales (JVM, Python VM)

## ARQUITECTURA DEL SISTEMA

### Componentes Principales

```
NuevoCompiladorPila/
├── pila.py              # Implementación de la estructura de datos pila
├── instrucciones.py     # Definición del lenguaje máquina (bytecode)
├── maquina_virtual.py  # Motor de ejecución del bytecode
├── ejemplo.py          # Demostración completa del sistema
└── README.md           # Esta documentación
```

### Función de Cada Componente

#### 1. **pila.py** - Estructura de Datos Fundamental
- **FUNCIÓN**: Almacenamiento temporal de operandos y resultados
- **IMPORTANCIA**: Es el corazón de las máquinas virtuales basadas en pila
- **CARACTERÍSTICAS**: Operaciones push, pop, peek con documentación detallada

#### 2. **instrucciones.py** - Lenguaje Máquina
- **FUNCIÓN**: Define el conjunto de instrucciones que el compilador genera
- **IMPORTANCIA**: Es el resultado final del proceso de compilación
- **INSTRUCCIONES**: Operaciones aritméticas, manejo de variables, control de flujo

#### 3. **maquina_virtual.py** - Motor de Ejecución
- **FUNCIÓN**: Ejecuta el bytecode generado por el compilador
- **IMPORTANCIA**: Separa el análisis del código fuente de su ejecución
- **ARQUITECTURA**: Pila + Memoria + Instruction Pointer

#### 4. **ejemplo.py** - Demostración Completa
- **FUNCIÓN**: Muestra el proceso completo de compilación y ejecución
- **IMPORTANCIA**: Permite entender cómo interactúan todos los componentes
- **EJEMPLOS**: Expresiones matemáticas y manejo de variables

## PROCESO DE COMPILACIÓN

### 1. Análisis de la Expresión
```
Código fuente: resultado = (10 + 5) * (8 - 3)
```

### 2. Conversión a Notación Postfija (RPN)
```
Notación postfija: 10 5 + 8 3 - *
```

### 3. Generación de Bytecode
```
PUSH_CONST 10
PUSH_CONST 5
ADD
PUSH_CONST 8
PUSH_CONST 3
SUB
MUL
STORE "resultado"
LOAD "resultado"
PRINT
HALT
```

### 4. Ejecución en la Máquina Virtual
La máquina virtual ejecuta cada instrucción modificando la pila y la memoria.

## EJECUCIÓN DEL PROYECTO

### Prerrequisitos
- Python 3.7 o superior
- No se requieren dependencias externas

### Ejecutar la Demostración
```bash
cd NuevoCompiladorPila
python ejemplo.py
```

### Salida Esperada
```
DEMOSTRACIÓN DEL COMPILADOR DE PILA
============================================================

=== EXPRESIÓN MATEMÁTICA: (10 + 5) * (8 - 3) ===
BYTECODE GENERADO:
POS  INSTRUCCIÓN      DESCRIPCIÓN
--------------------------------------------------
00   PUSH_CONST 10   Apilar constante 10
01   PUSH_CONST 5    Apilar constante 5
02   ADD             Sumar: a + b
03   PUSH_CONST 8    Apilar constante 8
04   PUSH_CONST 3    Apilar constante 3
05   SUB             Restar: a - b
06   MUL             Multiplicar: a * b
07   STORE resultado  Almacenar en variable 'resultado'
08   LOAD resultado   Cargar variable 'resultado'
09   PRINT           Imprimir valor
10   HALT            Detener ejecución

EJECUTANDO PROGRAMA 1:
OUTPUT: 75

=== PROGRAMA CON VARIABLES ===
...

EJECUTANDO PROGRAMA 2:
OUTPUT: 31

DEMOSTRACIÓN COMPLETADA CON ÉXITO
```

## EJEMPLOS DETALLADOS

### Ejemplo 1: Expresión Matemática Compleja
**Expresión**: `(10 + 5) * (8 - 3) = 75`

**Ejecución paso a paso**:
1. `PUSH 10` → `[10]`
2. `PUSH 5` → `[10, 5]`
3. `ADD` → `[15]`
4. `PUSH 8` → `[15, 8]`
5. `PUSH 3` → `[15, 8, 3]`
6. `SUB` → `[15, 5]`
7. `MUL` → `[75]`

### Ejemplo 2: Manejo de Variables
**Programa**:
```python
x = 7
y = 3
z = x * y + 10  # z = 7 * 3 + 10 = 31
print(z)
```

## CONCEPTOS CLAVE APRENDIDOS

### 1. **Máquinas Virtuales Basadas en Pila**
- No necesitan registros explícitos
- Todas las operaciones usan la pila
- Usadas por JVM, Python VM, .NET IL

### 2. **Bytecode**
- Representación intermedia del código
- Independiente de la plataforma
- Fácil de optimizar

### 3. **Notación Postfija (RPN)**
- Elimina la necesidad de paréntesis
- Facilita la evaluación de expresiones
- Base de las calculadoras HP

### 4. **Separación de Responsabilidades**
- Compilador: Análisis y generación de código
- Máquina Virtual: Ejecución del código
- Memoria: Almacenamiento de variables

## RELACIÓN CON COMPILADORES REALES

Este proyecto simplifica conceptos usados en compiladores profesionales:

| Concepto del Proyecto | Compilador Real |
|----------------------|-----------------|
| Nuestro OpCode | JVM bytecode, Python bytecode |
| Nuestra Pila | JVM operand stack, Python evaluation stack |
| Nuestra Memoria | JVM heap, Python object space |
| Nuestra Máquina Virtual | JVM, CPython interpreter |

## EXTENSIONES POSIBLES

- [ ] Análisis léxico y sintáctico completo
- [ ] Soporte para tipos de datos adicionales
- [ ] Operaciones de comparación y saltos condicionales
- [ ] Funciones y llamadas a procedimientos
- [ ] Optimización de bytecode
- [ ] Depurador integrado

## REFERENCIAS

- *Compilers: Principles, Techniques, and Tools* - Aho, Lam, Sethi, Ullman
- *Programming Language Pragmatics* - Michael L. Scott
- Java Virtual Machine Specification
- Python Bytecode Documentation

---

**Proyecto educativo creado para entender los fundamentos de la compilación**
