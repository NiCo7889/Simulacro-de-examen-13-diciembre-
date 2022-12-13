# Escriba una rotate que gire una matriz bidimensional (una matriz) ya sea en sentido horario o antihorario 
# 90 grados y devuelva la matriz rotada. La función acepta dos parámetros: una matriz y una cadena que 
# especifica la dirección o rotación. La dirección será "clockwise"o "counter-clockwise".

random matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate(matrix, direction):
    if direction == "clockwise":
        return list(zip(*matrix[::-1]))
    elif direction == "counter-clockwise":
        return list(zip(*matrix))[::-1]
    else:
        return "Error"

print(rotate(matrix, "clockwise"))
print(rotate(matrix, "counter-clockwise"))
