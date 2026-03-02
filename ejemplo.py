from typing import List
from instrucciones import Instruccion, OpCode
from maquina_virtual import MaquinaVirtual

class CompiladorSimple:
    """
    COMPILADOR SENCILLO - DEMOSTRACIÓN EDUCATIVA
    
    FUNCIÓN EN EL PROCESO DE COMPILACIÓN:
    Transforma expresiones matemáticas simples en bytecode que
    la máquina virtual puede ejecutar. Es una versión simplificada
    de un compilador real.
    
    IMPORTANCIA:
    - Demuestra el proceso de análisis y generación de código
    - Muestra cómo las expresiones se convierten en operaciones de pila
    - Es el puente entre el lenguaje humano y el lenguaje máquina
    
    NOTA: Este es un compilador educativo que trabaja con expresiones
    predefinidas, no con análisis léxico completo.
    """
    
    @staticmethod
    def compilar_expresion_simple() -> List[Instruccion]:
        """
        Compila la expresión: resultado = (10 + 5) * (8 - 3)
        
        PASOS DE COMPILACIÓN:
        1. Analizar la expresión matemática
        2. Convertir a notación postfija (RPN)
        3. Generar bytecode para máquina de pila
        
        EXPRESIÓN: (10 + 5) * (8 - 3)
        RPN: 10 5 + 8 3 - *
        BYTECODE:
        """
        programa = [
            # Calcular (10 + 5)
            Instruccion(OpCode.PUSH_CONST, 10),  # [10]
            Instruccion(OpCode.PUSH_CONST, 5),   # [10, 5]
            Instruccion(OpCode.ADD),              # [15]
            
            # Calcular (8 - 3)
            Instruccion(OpCode.PUSH_CONST, 8),    # [15, 8]
            Instruccion(OpCode.PUSH_CONST, 3),   # [15, 8, 3]
            Instruccion(OpCode.SUB),              # [15, 5]
            
            # Multiplicar resultados
            Instruccion(OpCode.MUL),              # [75]
            
            # Almacenar en variable
            Instruccion(OpCode.STORE, "resultado"),
            
            # Imprimir resultado
            Instruccion(OpCode.LOAD, "resultado"),
            Instruccion(OpCode.PRINT),
            
            # Finalizar programa
            Instruccion(OpCode.HALT)
        ]
        
        return programa
    
    @staticmethod
    def compilar_programa_variables() -> List[Instruccion]:
        """
        Compila un programa con manejo de variables:
        
        x = 7
        y = 3
        z = x * y + 10
        print(z)
        
        DEMUESTRA:
        - Declaración y asignación de variables
        - Uso de variables en expresiones
        - Operaciones combinadas
        """
        programa = [
            # x = 7
            Instruccion(OpCode.PUSH_CONST, 7),
            Instruccion(OpCode.STORE, "x"),
            
            # y = 3
            Instruccion(OpCode.PUSH_CONST, 3),
            Instruccion(OpCode.STORE, "y"),
            
            # Calcular z = x * y + 10
            Instruccion(OpCode.LOAD, "x"),        # [x]
            Instruccion(OpCode.LOAD, "y"),        # [x, y]
            Instruccion(OpCode.MUL),              # [x*y]
            Instruccion(OpCode.PUSH_CONST, 10),   # [x*y, 10]
            Instruccion(OpCode.ADD),              # [x*y+10]
            Instruccion(OpCode.STORE, "z"),
            
            # Imprimir z
            Instruccion(OpCode.LOAD, "z"),
            Instruccion(OpCode.PRINT),
            
            Instruccion(OpCode.HALT)
        ]
        
        return programa

def mostrar_programa(programa: List[Instruccion], titulo: str) -> None:
    """
    Muestra el bytecode generado de forma legible.
    
    FUNCIÓN: Facilita la comprensión del código compilado.
    IMPORTANCIA: Permite verificar el resultado del proceso de compilación.
    """
    print(f"\n=== {titulo} ===")
    print("BYTECODE GENERADO:")
    print("POS  INSTRUCCIÓN      DESCRIPCIÓN")
    print("-" * 50)
    
    for i, instr in enumerate(programa):
        descripcion = _describir_instruccion(instr)
        print(f"{i:02d}   {str(instr):<15}   {descripcion}")

def _describir_instruccion(instruccion: Instruccion) -> str:
    """Genera una descripción legible de cada instrucción."""
    descripciones = {
        OpCode.PUSH_CONST: f"Apilar constante {instruccion.argumento}",
        OpCode.POP: "Desapilar valor",
        OpCode.ADD: "Sumar: a + b",
        OpCode.SUB: "Restar: a - b", 
        OpCode.MUL: "Multiplicar: a * b",
        OpCode.DIV: "Dividir: a / b",
        OpCode.STORE: f"Almacenar en variable '{instruccion.argumento}'",
        OpCode.LOAD: f"Cargar variable '{instruccion.argumento}'",
        OpCode.PRINT: "Imprimir valor",
        OpCode.HALT: "Detener ejecución"
    }
    
    return descripciones.get(instruccion.opcode, "Instrucción desconocida")

def ejecutar_demostracion() -> None:
    """
    FUNCIÓN PRINCIPAL - DEMOSTRACIÓN COMPLETA
    
    Muestra el proceso completo de compilación y ejecución:
    1. Compilación de expresiones a bytecode
    2. Visualización del código generado
    3. Ejecución en la máquina virtual
    4. Resultado final
    """
    print("DEMOSTRACIÓN DEL COMPILADOR DE PILA")
    print("=" * 60)
    
    # Demostración 1: Expresión matemática compleja
    compilador = CompiladorSimple()
    programa1 = compilador.compilar_expresion_simple()
    mostrar_programa(programa1, "EXPRESIÓN MATEMÁTICA: (10 + 5) * (8 - 3)")
    
    print("\nEJECUTANDO PROGRAMA 1:")
    maquina = MaquinaVirtual()
    maquina.ejecutar(programa1)
    
    # Demostración 2: Programa con variables
    programa2 = compilador.compilar_programa_variables()
    mostrar_programa(programa2, "PROGRAMA CON VARIABLES")
    
    print("\nEJECUTANDO PROGRAMA 2:")
    maquina2 = MaquinaVirtual()
    maquina2.ejecutar(programa2)
    
    print("\nDEMOSTRACIÓN COMPLETADA CON ÉXITO")

if __name__ == "__main__":
    ejecutar_demostracion()
