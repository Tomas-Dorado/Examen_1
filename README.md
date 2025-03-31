# Examen_1

https://github.com/Tomas-Dorado/Examen_1.git

# Examen_1

Este proyecto implementa una serie de clases y funciones en Python para trabajar con puntos y rectángulos en un plano cartesiano. El objetivo es demostrar conceptos básicos de programación orientada a objetos, como clases, métodos y encapsulación.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- **`Punto.py`**: Define la clase `Punto`, que representa un punto en el plano cartesiano. Incluye métodos para calcular el cuadrante, vectores y distancias entre puntos.
- **`Rectangulo.py`**: Define la clase `Rectangulo`, que representa un rectángulo en el plano cartesiano. Incluye métodos para calcular la base, altura y área del rectángulo.
- **`main.py`**: Contiene el punto de entrada del programa. Aquí se crean instancias de las clases `Punto` y `Rectangulo`, y se realizan diversas operaciones para demostrar su funcionalidad.
- **`README.md`**: Este archivo, que describe el proyecto.

## Clases y Funcionalidades

### Clase `Punto` (definida en `Punto.py`)

La clase `Punto` incluye las siguientes funcionalidades:

- **Constructor**: Permite inicializar un punto con coordenadas `x` e `y`.
- **Método `cuadrante`**: Determina en qué cuadrante del plano cartesiano se encuentra el punto.
- **Método `vector`**: Calcula el vector entre dos puntos.
- **Método `distancia`**: Calcula la distancia euclidiana entre dos puntos.
- **Representación**: Sobrescribe el método `__str__` para mostrar el punto en formato `(x, y)`.

### Clase `Rectangulo` (definida en `Rectangulo.py`)

La clase `Rectangulo` incluye las siguientes funcionalidades:

- **Constructor**: Permite inicializar un rectángulo con dos puntos: `punto_inicial` y `punto_final`.
- **Método `base`**: Calcula la longitud de la base del rectángulo.
- **Método `altura`**: Calcula la altura del rectángulo.
- **Método `area`**: Calcula el área del rectángulo.
- **Representación**: Sobrescribe el método `__str__` para mostrar el rectángulo en formato `Rectángulo: (x1, y1) a (x2, y2)`.

### Archivo `main.py`

El archivo `main.py` demuestra el uso de las clases `Punto` y `Rectangulo` mediante las siguientes operaciones:

1. Creación de puntos en el plano cartesiano.
2. Impresión de las coordenadas de los puntos.
3. Determinación del cuadrante de varios puntos.
4. Cálculo de vectores entre puntos.
5. Cálculo de distancias entre puntos.
6. Identificación del punto más lejano del origen.
7. Creación de un rectángulo a partir de dos puntos y cálculo de su base, altura y área.

## Ejecución del Programa

Para ejecutar el programa, asegúrate de tener Python instalado en tu sistema. Luego, ejecuta el archivo `main.py`:

```bash
python [main.py](http://_vscodecontentref_/0)