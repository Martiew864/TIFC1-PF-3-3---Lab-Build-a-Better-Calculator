def main():

  print("Hello learners!")
def addmultiplenumbers(numbers):
    """Suma todos los números de la lista."""
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    """Multiplica cada número por el siguiente."""
    if not numbers:
        return None
    
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    """Devuelve True si el número es par, False si no lo es."""
    # Primero verificamos si es entero
    if isinstance(num, int) and num % 2 == 0:
        return True
    return False


def isitaninteger(num):
    """Devuelve True si el valor es un número entero."""
    return isinstance(num, int)

def main():
    print("Hello learners!")
    print("Probemos nuestras funciones...\n")

    # ------------------------------
    # Entrada para suma
    # ------------------------------
    nums_str = input("Ingresa números separados por coma para SUMAR: ")
    nums_list = [float(x) for x in nums_str.split(",")]
    print("Resultado de la suma:", addmultiplenumbers(nums_list))

    # ------------------------------
    # Entrada para multiplicación
    # ------------------------------
    nums_str = input("\nIngresa números separados por coma para MULTIPLICAR: ")
    nums_list = [float(x) for x in nums_str.split(",")]
    print("Resultado de la multiplicación:", multiplymultiplenumbers(nums_list))

    # ------------------------------
    # Entrada para isiteven
    # ------------------------------
    num_str = input("\nIngresa un número para saber si es par: ")
    
    # Intentamos convertirlo a entero si se puede
    try:
        num = int(num_str)
    except ValueError:
        num = float(num_str)

    print("¿Es par?", isiteven(num))

    # ------------------------------
    # Entrada para isitaninteger
    # ------------------------------
    num_str = input("\nIngresa un número para saber si es entero: ")

    try:
        num = int(num_str)
        print("¿Es entero?", isitaninteger(num))
    except ValueError:
        num = float(num_str)
        print("¿Es entero?", isitaninteger(num))


if __name__=="__main__":
  main()