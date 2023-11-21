import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lista = [1, 2, 3, 4]
    x = np.array(lista)
    print(x)
    print()
    print()
    # guardando en un archivo
    a = np.random.randint(10, size=(3, 3))
    np.save("nomArchivo", a)
    #---- se lee del archivo
    a = np.load("nomArchivo.npy")
    print(a)
    #----sistema lineal
    print("Resuelve un sistema de ecuaciones")
    A = np.array([[3, 7, -5],
                  [2, -4, 3],
                  [1, 3, -5]])

    b = np.array([10, 8, 9])
    x = np.linalg.solve(A, b)
    print(x)
    #----devuelve la estructura de un arreglo
    C = np.array([[3, 7, -5],
                  [2, -4, 3],
                  [1, 3, -5],
                  [2, 4, -7]])
    print(C.shape)
    #---devuelve las dimensiones de un arreglo
    C = np.array([[3, 7, -5],
                  [2, -4, 3],
                  [1, 3, -5],
                  [2, 4, -7]])
    print(C.ndim)
    #----crea un arreglo en base aun rango
    D = np.arange(10, 55, 3)
    print(D)
    #---modifica la estructura
    D = np.arange(10, 55, 3)
    D = D.reshape(5, 3)
    print(D)
    #----
    #--- suma los elementos de un arreglo
    print()
    print()
    arreglo1 = np.array([[10, 25, 12],
                         [4, 1, 23]])
    arreglo2 = np.array([[9, 10, 13],
                         [16, 14, 17]])
    arraySuma = arreglo1 + arreglo2
    print("suma de dos arreglos: ")
    print(arraySuma)
   #--- resta los elementos de un arreglo
    print()
    print()
    arreglo1 = np.array([[10, 25, 12],
                         [4, 1, 23]])
    arreglo2 = np.array([[9, 10, 13],
                         [16, 14, 17]])
    arraySuma = arreglo2 -  arreglo1
    print("resta dos arreglos")
    print(arraySuma)
    #--- permite su dividir
    print()
    print()
    print("Creamos un arreglo de 16X3")
    Arreglo = np.arange(20, 68, 1)
    Arreglo = Arreglo.reshape(16, 3)
    print(Arreglo)

    print("\nDividiendo en 4 sub arrays\n")
    subArreglos = np.split(Arreglo, 4)
    print(subArreglos)

    #----Delete: permite eliminar tanto filas como columnas del arreglo
    print()
    print()
    Arreglo = np.array([[20, 40, 60],
                        [80, 100, 110],
                        [120, 130, 140]])

    Arreglo = np.delete(Arreglo, 1, axis=0)
    print(Arreglo)

    #------Insert: permite agregar elementos al arreglo
    print()
    print()
    add = np.array([[500, 510, 520]])
    Arreglo = np.insert(Arreglo, 1, add, axis=0)
    print(Arreglo)
