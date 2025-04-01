import math

def lanzador():
    # Crear los puntos
    A = (2, 3)
    B = (5, 5)
    C = (-3, -1)
    D = (0, 0)

    # Imprimir los puntos
    print(f"Punto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

    # Determinar el cuadrante de un punto
    def cuadrante(punto):
        x, y = punto
        if x > 0 and y > 0:
            return "Primer cuadrante"
        elif x < 0 and y > 0:
            return "Segundo cuadrante"
        elif x < 0 and y < 0:
            return "Tercer cuadrante"
        elif x > 0 and y < 0:
            return "Cuarto cuadrante"
        else:
            return "Sobre un eje o el origen"

    # Consultar cuadrantes
    print(f"El punto A está en el {cuadrante(A)}")
    print(f"El punto C está en el {cuadrante(C)}")
    print(f"El punto D está en el {cuadrante(D)}")

    # Calcular vectores
    def vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

    AB = vector(A, B)
    BA = vector(B, A)
    print(f"Vector AB: {AB}")
    print(f"Vector BA: {BA}")

    # Calcular distancia entre dos puntos
    def distancia(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    distancia_AB = distancia(A, B)
    distancia_BA = distancia(B, A)
    print(f"Distancia entre A y B: {distancia_AB}")
    print(f"Distancia entre B y A: {distancia_BA}")

    # Determinar el punto más lejano del origen
    def distancia_origen(punto):
        return math.sqrt(punto[0]**2 + punto[1]**2)

    distancias = {"A": distancia_origen(A), "B": distancia_origen(B), "C": distancia_origen(C)}
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")

    # Crear un rectángulo con A y B
    base = abs(B[0] - A[0])
    altura = abs(B[1] - A[1])
    area = base * altura
    print(f"Base del rectángulo: {base}")
    print(f"Altura del rectángulo: {altura}")
    print(f"Área del rectángulo: {area}")
