#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifica la instalación de las dependencias del curso
Métodos numéricos para ecuaciones en derivadas parciales.

@author: Nicolas Guarin-Zapata
@date: Febrero 2026
"""
import numpy as np

## Datos de prueba: `peaks()` de Matlab
x, y = np.mgrid[-3:3:150j,-3:3:150j]
z =  3*(1 - x)**2 * np.exp(-x**2 - (y + 1)**2) \
   - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) \
   - 1./3*np.exp(-(x + 1)**2 - y**2)

   #%% Matplotlib
try:
    msg = "Comprobando la instalación de Matplotlib"
    print(msg)
    print("="*len(msg))
    import matplotlib.pyplot as plt
    from matplotlib.colors import LightSource

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Create light source object.
    ls = LightSource(azdeg=0, altdeg=65)
    rgb = ls.shade(z, plt.cm.RdYlBu)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0,
                           antialiased=False, facecolors=rgb)
    plt.show()
    print("¡Matplotlib está funcionando correctamente!")
except:
    print("¡Matplotlib no está funcionando correctamente!")


#%% Matplotlib
try:
    msg = "Comprobando la instalación de Matplotlib"
    print(msg)
    print("="*len(msg))
    import matplotlib.pyplot as plt
    from matplotlib.colors import LightSource

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Create light source object.
    ls = LightSource(azdeg=0, altdeg=65)
    rgb = ls.shade(z, plt.cm.RdYlBu)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0,
                           antialiased=False, facecolors=rgb)
    plt.show()
    print("¡Matplotlib está funcionando correctamente!")
except:
    print("¡Matplotlib no está funcionando correctamente!")




#%% PyVista
try:
    msg = "Comprobando la instalación de PyVista"
    print("\n\n" + msg)
    print("="*len(msg))
    import pyvista as pv

    grid = pv.StructuredGrid(x, y, z)
    plotter = pv.Plotter()
    plotter.add_mesh(grid, scalars=z.ravel(), cmap='RdYlBu',
                     show_edges=False)
    plotter.show()
    print("¡PyVista está funcionando correctamente!")
except:
    print("¡PyVista no está funcionando correctamente!")
