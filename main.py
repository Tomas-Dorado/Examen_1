from Punto import Punto
from Rectangulo import Rectangulo


def main():
    # Crear los puntos
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir los puntos
    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

    # Consultar cuadrantes
    print("\nCuadrantes:")
    print(f"A pertenece al cuadrante: {A.cuadrante()}")
    print(f"C pertenece al cuadrante: {C.cuadrante()}")
    print(f"D pertenece al cuadrante: {D.cuadrante()}")

    # Calcular vectores AB y BA
    AB = A.vector(B)
    BA = B.vector(A)

    print("\nVectores:")
    print(f"Vector AB: {AB}")
    print(f"Vector BA: {BA}")

    # Calcular distancias
    dist_AB = A.distancia(B)
    dist_BA = B.distancia(A)

    print("\nDistancias:")
    print(f"Distancia entre A y B: {dist_AB}")
    print(f"Distancia entre B y A: {dist_BA}")

    # Determinar el punto más lejano del origen
    distancias = {"A": A.distancia(D), "B": B.distancia(D), "C": C.distancia(D)}
    punto_mas_lejano = max(distancias, key=distancias.get)

    print("\nPunto más lejano del origen:")
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)
    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

if __name__ == "__main__":
    main()