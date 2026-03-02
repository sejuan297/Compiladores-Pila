from typing import List
from instrucciones import Instruccion, OpCode
from maquina_virtual import MaquinaVirtual

class CompiladorPila:
    """Compilador de pila interactivo."""
    
    def __init__(self):
        self.variables = {}
    
    def infija_a_postfija(self, expresion: str) -> List[str]:
        """Convierte expresión infija a notación postfija (RPN)."""
        import re
        
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        tokens = re.findall(r'(\d+\.?\d*|[+\-*/()])', expresion.replace(' ', ''))
        
        salida = []
        pila_operadores = []
        
        for token in tokens:
            if token.replace('.', '').isdigit():
                salida.append(token)
            elif token in precedencia:
                while (pila_operadores and pila_operadores[-1] != '(' and
                       precedencia.get(pila_operadores[-1], 0) >= precedencia[token]):
                    salida.append(pila_operadores.pop())
                pila_operadores.append(token)
            elif token == '(':
                pila_operadores.append(token)
            elif token == ')':
                while pila_operadores and pila_operadores[-1] != '(':
                    salida.append(pila_operadores.pop())
                if pila_operadores and pila_operadores[-1] == '(':
                    pila_operadores.pop()
        
        while pila_operadores:
            salida.append(pila_operadores.pop())
        
        return salida
    
    def compilar_expresion(self, expresion: str, nombre_variable: str = "resultado") -> List[Instruccion]:
        """Compila una expresión matemática a bytecode."""
        postfija = self.infija_a_postfija(expresion)
        programa = []
        
        for token in postfija:
            if token.replace('.', '').isdigit():
                programa.append(Instruccion(OpCode.PUSH_CONST, float(token)))
            elif token == '+':
                programa.append(Instruccion(OpCode.ADD))
            elif token == '-':
                programa.append(Instruccion(OpCode.SUB))
            elif token == '*':
                programa.append(Instruccion(OpCode.MUL))
            elif token == '/':
                programa.append(Instruccion(OpCode.DIV))
        
        programa.append(Instruccion(OpCode.STORE, nombre_variable))
        programa.append(Instruccion(OpCode.LOAD, nombre_variable))
        programa.append(Instruccion(OpCode.PRINT))
        programa.append(Instruccion(OpCode.HALT))
        
        return programa

def mostrar_programa(programa: List[Instruccion], expresion: str) -> None:
    """Muestra el bytecode generado."""
    print(f"\n=== EXPRESIÓN: {expresion} ===")
    print("BYTECODE GENERADO:")
    print("POS  INSTRUCCIÓN      DESCRIPCIÓN")
    print("-" * 50)
    
    descripciones = {
        OpCode.PUSH_CONST: lambda arg: f"Apilar constante {arg}",
        OpCode.POP: lambda arg: "Desapilar valor",
        OpCode.ADD: lambda arg: "Sumar: a + b",
        OpCode.SUB: lambda arg: "Restar: a - b", 
        OpCode.MUL: lambda arg: "Multiplicar: a * b",
        OpCode.DIV: lambda arg: "Dividir: a / b",
        OpCode.STORE: lambda arg: f"Almacenar en variable '{arg}'",
        OpCode.LOAD: lambda arg: f"Cargar variable '{arg}'",
        OpCode.PRINT: lambda arg: "Imprimir valor",
        OpCode.HALT: lambda arg: "Detener ejecución"
    }
    
    for i, instr in enumerate(programa):
        descripcion = descripciones.get(instr.opcode, lambda arg: "Instrucción desconocida")(instr.argumento)
        print(f"{i:02d}   {str(instr):<15}   {descripcion}")

def interfaz_interactiva():
    """Interfaz principal del compilador interactivo."""
    compilador = CompiladorPila()
    
    print("=" * 60)
    print("COMPILADOR DE PILA INTERACTIVO")
    print("=" * 60)
    print("Operaciones soportadas: +, -, *, /")
    print("Puedes usar paréntesis: ( )")
    print("Escribe 'ayuda' para ver ejemplos")
    print("Escribe 'salir' para terminar")
    print("-" * 60)
    
    while True:
        try:
            entrada = input("\n> ").strip()
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("¡Hasta luego!")
                break
            
            if entrada.lower() == 'ayuda':
                print("\n=== EJEMPLOS ===")
                print("2 + 3")
                print("(2 + 3) * 4")
                print("10 + 5 * 2")
                print("(100 - 50) / (25 + 25)")
                continue
            
            if entrada.lower() == 'demo':
                print("\n=== DEMOSTRACIÓN ===")
                expresion1 = "(10 + 5) * (8 - 3)"
                programa1 = compilador.compilar_expresion(expresion1)
                mostrar_programa(programa1, expresion1)
                print(f"\nEJECUTANDO: {expresion1}")
                maquina1 = MaquinaVirtual()
                maquina1.ejecutar(programa1)
                continue
            
            if not entrada:
                print("Por favor ingresa una expresión válida.")
                continue
            
            programa = compilador.compilar_expresion(entrada)
            mostrar_programa(programa, entrada)
            
            print(f"\nEJECUTANDO: {entrada}")
            maquina = MaquinaVirtual()
            maquina.ejecutar(programa)
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Por favor verifica tu expresión e intenta de nuevo.")

if __name__ == "__main__":
    interfaz_interactiva()
