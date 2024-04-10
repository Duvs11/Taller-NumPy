import numpy as np
# importa la biblioteca (numpy) y le da un alias (np)
import matplotlib.pyplot as plt
# importa el módulo (pyplot) de la biblioteca (matplotlib) y le da ela lias(plt)
def mandelbrot(h, w, maxit=20, r=2):
# define la función (mnddelbrot) y establece valores predeterminados
# maxit=20 y r=2, son valores predeterminados
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
# es una cadena de documentación (docstring) que describe lo que hace la función mandelbrot
    x = np.linspace(-2.5, 1.5, 4*h+1)
# define un arreglo de -2.5 a 1.5 equidistantes por 4*h+1 que depende del parametro inicial de mandelbrot (h)
    y = np.linspace(-1.5, 1.5, 3*w+1)
# define un arreglo de -1.5 a 1.5 equidistantes por 3*w+1 que depende del parametro inicial de mandelbrot (w)
    A, B = np.meshgrid(x, y)
# se asigna una lista de matrices de coordenadas a partir de vectores de coordenadas unidimensionales en (A, B)
    C = A + B*1j
# suma los valores de A y B*1*J y se los asigna a la variable C
    z = np.zeros_like(C)
# crea un areglo lleno de ceros con las caracteristicas de (c)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))