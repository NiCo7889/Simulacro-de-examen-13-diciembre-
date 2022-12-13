# En algunos países de la antigua Unión Soviética existía la creencia de los boletos de la
# suerte. Se creía que un billete de transporte de cualquier tipo traía suerte si la suma de los
# dígitos de la mitad izquierda de su número era igual a la suma de los dígitos de la mitad
# derecha. Aquí hay ejemplos de tales números:

# 003111    # 3 = 1 + 1 + 1
# 813372    # 8 + 1 + 3 = 3 + 7 + 2
# 17935     # 1 + 7 = 3 + 5 // si la longitud es impar, debes ignorar el número del medio al sumar las mitades.
# 56328116  # 5 + 6 + 3 = 2 + 8 + 1 + 1

# Dichos boletos se comían después de usarlos o se recolectaban para fanfarronear.
# Su tarea es escribir una función luck_check(str), que devuelve true/Truesi el argumento es una
# representación decimal de cadena de un número de boleto de la suerte, o false/Falsepara
# todos los demás números. Debería arrojar errores para cadenas vacías o cadenas que no
# representan un número decimal.


def luck_check(str):
    if str == "":
        return "Error"
    else:
        if len(str) % 2 == 0:
            a = 0
            b = 0
            for i in range(0, len(str) // 2):
                a += int(str[i])
            for i in range(len(str) // 2, len(str)):
                b += int(str[i])
            if a == b:
                return True
            else:
                return False
        else:
            a = 0
            b = 0
            for i in range(0, len(str) // 2):
                a += int(str[i])
            for i in range(len(str) // 2 + 1, len(str)):
                b += int(str[i])
            if a == b:
                return True
            else:
                return False

print(luck_check("003111"))
print(luck_check("813372"))
print(luck_check("17935"))
print(luck_check("56328116"))

