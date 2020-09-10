# File de prueba para primer commit




def basic_ops_auxiliar(x, y, operation): #
    if operation == 1:
        result = x + y
        return result
    elif operation == 2:
        result = x - y
        return result
    elif operation == 3:
        result = x & y
        return result
    elif operation == 4:
        result = x | y
        return result


class operations:
    def __init__(self):
        pass

    def basic_ops(self):
        try:
            x = int(input("Digite el primer número: "))
            y = int(input("Digite el segundo número: "))

            if x not in range(-127, 128) or y not in range(-127, 128):
                print("ERROR: Ingrese números en el rango [-127,127]")
                exit()
            operation = int(input("""Ingrese el NUMERO de la operación que desea realizar: 
                     1 - Suma
                     2 - Resta
                     3 - AND
                     4 - OR
        Operación a realizar: """))

            if operation not in range(1, 5):
                print("ERROR: Ingrese una operación válida (de 1 a 4)")
                exit()

            result = basic_ops_auxiliar(x, y, operation)
            print("El resultado es: ", result)

        except ValueError:
            print("ERROR: Ingrese solamente números enteros")
            exit()

