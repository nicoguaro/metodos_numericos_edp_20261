#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Description

@author: Nicolas Guarin-Zapata
@date: Wed Feb 28 10:24:59 2018
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.bottom"] = False
plt.rcParams["axes.spines.left"] = False


def line_plots(x, y, x0, h, fun, lines, highlight_line):
     plt.plot(x, y, lw=2)
     plt.plot([x0 - h, x0, x0 + h], fun([x0 - h, x0, x0 + h]),
              "ok", zorder=4)
     plt.vlines([x0 -h, x0, x0 + h], 0, fun([x0 -h, x0, x0 + h]),
                zorder=2, color=gray, lw=1)
     plt.text(x0 - h, 0, u"$x_0 - h$",
              horizontalalignment="center",
              verticalalignment="top")
     plt.text(x0, 0, u"$x_0$",
              horizontalalignment="center",
              verticalalignment="top")
     plt.text(x0 + h, 0, u"$x_0 + h$",
              horizontalalignment="center",
              verticalalignment="top")
     for cont, line in enumerate(lines):
         if cont == highlight_line:
             plt.plot(x, line, lw=2, zorder=3)
         else:
             plt.plot(x, line, color=gray, lw=1, zorder=2)


gray = "#969696"
fun = lambda x: np.sin(np.pi*np.asarray(x))
der = lambda x: np.pi * np.cos(np.pi*np.asarray(x))
x = np.linspace(0.2, 1.2)
y = fun(x)
h = 0.2
x0 = 0.7
xm = x0 - h
xp = x0 + h
rectam = (fun(x0) - fun(xm))*(x - xm)/(x0 - xm) + fun(xm)
rectap = (fun(xp) - fun(x0))*(x - x0)/(xp - x0) + fun(x0)
recta0 = (fun(xp) - fun(xm))*(x - xm)/(xp - xm) + fun(xm)
recta_tan = der(x0)*(x - x0) + fun(x0)
titles = [u"Pendiente $u'(x_0)$", u"Pendiente $D_{-}u(x)$",
          u"Pendiente $D_{+}(x)$", u"Pendiente $D_{0} u(x)$"]

plt.figure(figsize=(8,5))
for cont in range(4):
    ax = plt.subplot(2,2, cont + 1)
    line_plots(x, y, x0, h, fun, [recta_tan, rectam, rectap, recta0],
               cont)
    ax.set_title(titles[cont])
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])

plt.savefig("ejemplo_diferencias_finitas.svg", transparent=True,
            bbox_inches="tight")
