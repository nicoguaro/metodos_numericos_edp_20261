"""
 Solve the reaction-diffusion equation for the Gray-Scott model on
 a periodic domain
 
   u_t = D_u lap(u) - u v² + f (1 - u)
   v_t = D_v lap(v) + u v² - (f + k) v
 
 @author: Nicolás Guarín-Zapata
 @date: October 2024
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


def one_iter(u, v, Du, Dv, f, k, dt, dx):
    A = u.copy()
    B = v.copy()

    A = A + dt*(Du*(np.roll(A, 1, axis=0) + np.roll(A, -1, axis=0)
                     + np.roll(A, 1, axis=1) + np.roll(A, -1, axis=1)- 4*A)/dx**2
                - A * B**2 + f*(1 - A))
    B = B + dt*(Dv*(np.roll(B, 1, axis=0) + np.roll(B, -1, axis=0)
                     + np.roll(B, 1, axis=1) + np.roll(B, -1, axis=1) - 4*B)/dx**2
                + A * B**2 - (f + k)*B)
    return A, B


def compute_niter(u, v, dx, dt, niter, Du=0.01, Dv=0.005, f=0.014, k=0.054,
                  frameskip=100, saveframes=True, ndigits=5):
    cont = 0
    framecont = 0
    files = []
    if saveframes:
        plt.figure(figsize=(5, 5))
        file = f"reac_diff_{str(0).zfill(ndigits)}.png"
        plot_sol(v)
        plt.savefig(file, bbox_inches="tight", transparent=True)
        files.append(file)
    for n in range(niter):
        u, v = one_iter(u, v, Du, Dv, f, k, dt, dx)
        cont = cont + 1
        if saveframes and cont == frameskip:
            print(f"Iteration {n}/{niter}")
            framecont = framecont + 1
            cont = 0
            file = f"reac_diff_{str(framecont).zfill(ndigits)}.png"
            plt.cla()
            plot_sol(v)
            plt.savefig(file, bbox_inches="tight", transparent=True)
            files.append(file)
    return u, v, files


def plot_sol(u):
    plt.contourf(u, cmap="magma")
    plt.axis("image")
    plt.axis("off")
    return None


def save_gif_PIL(outfile, files, fps=20, loop=0):
    """Helper function for saving GIFs
    
    Parameters
    ----------
    outfile : string
        Path to the output file.
    files : list
        List of paths with the PNG files.
    fps : int (optional)
        Frames per second.
    loop : int
        The number of times the GIF should loop.
        0 means that it will loop forever.
    """
    imgs = [Image.open(file) for file in files]
    imgs[0].save(fp=outfile, format='GIF', append_images=imgs[1:],
                 save_all=True, duration=int(1000/fps), loop=loop)


#%%

# -------------------------------
# f = 0.082 ; k = 0.06 #  : Cerebro ; coral 
f = 0.058 ; k = 0.065 #  : rayas ; gusano
# f = 0.034 ; k = 0.0618 #  : leopardo
# f = 0.03  ; k = 0.062 #  : puntos auto replicantes
# f = 0.03  ; k = 0.0565 #  : laberintos
# f = 0.026 ; k = 0.051 #  : Manchas locas 
# f = 0.014 ; k = 0.047 #  :  (big waves)
# f = 0.018 ; k = 0.051 #  :  (small waves)
# f = 0.014 ; k = 0.054 #  :  (Moving spots (glider-like))

L = 60
nx = 280
ny = 280
Du = 0.01
Dv = 0.01/2
dx = L/nx
beta = 0.9
dt = 0.25 * beta * dx**2/ max(Du,Dv)
y, x = 60*np.mgrid[0:1:1j*ny, 0:1:1j*nx]


u = np.ones_like(x)
v = np.exp( -10*(x - 0.75*L)**2 - 10*(y - 0.5*L)**2)
# v = np.exp( -11*((x - L/3)**2 - (y - L/4)**2) )\
#     + np.exp( -11*((x - L/1.5)**2 - (y - L/2.3)**2) )\
#     + np.exp( -11*((x - L/2)**2 - (y - L/2)**2) )

niter = 50000
u, v, files = compute_niter(u, v, dx, dt, niter, f=f, k=k)

save_gif_PIL("reac_diff_line_anim.gif", files, fps=5, loop=0)

[os.remove(file) for file in files]

