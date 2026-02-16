"""
Verifica la instalación de las dependencias del curso
Métodos numéricos para ecuaciones en derivadas parciales.

Este archivo se basa en el siguiente script:

https://github.com/gforsyth/numba_tutorial_scipy2017/blob/master/check_install.py

publicado bajo licencia MIT por Gilbert Forsyth y Lorena Barba.

@date: Febrero 2026
"""
import importlib
import sys
from warnings import warn

onpy2 = False


try:
    assert sys.version_info >= (3,0)
    import importlib.util
except AssertionError:
    warn('Este curso está diseñado para Python 3. Python 2 no es compatible explícitamente.')
    onpy2 = True


def tuple_version(version):
    return tuple(int(x) for x in version.strip('<>+-=.').split('.'))


def check_versions():
    version_trouble=False
    mpl = importlib.import_module('matplotlib')
    mpl_version = tuple_version(mpl.__version__)
    if mpl_version < (2, 0, 0):
        print('Actualice matplotlib a la versión 2.0.0 o superior')
        version_trouble=True

    return version_trouble


def main():
    required_modules = ['numpy', 'matplotlib', 'jupyter', 'scipy',
                        'vtk', 'pyvista', 'sympy', 'meshio']
    
    missing_modules = []
    for mod in required_modules:
        if not onpy2:
            spec = importlib.util.find_spec(mod)
            if spec is None:
                missing_modules.append(mod)
        else:
            try:
                importlib.import_module(mod)
            except ImportError:
                missing_modules.append(mod)

    if missing_modules:
        print('Los siguientes módulos son necesarios pero no están instalados:')
        print('    {}'.format(', '.join(missing_modules)))
        print('\nPuede instalarlos usando conda ejecutando:')
        print('\n    conda install {}'.format(' '.join(missing_modules)))
        print('\nO puede instalarlos usando pip ejecutando:')
        print('\n    pip install {}'.format(' '.join(missing_modules)))
    else:
        if check_versions():
            print('Todos los paquetes están instalados pero al menos uno necesita actualizarse')
        else:
            print('¡Todo se ve bien!')


if __name__ == '__main__':
    main()
