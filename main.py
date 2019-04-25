import matplotlib as mpl
import sympy
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox
from BertnPoly import *

def addButtonClicked(event):
        spir.spin(radiobuttons_color.value_selected)
        ax.clear()
        #ax.plot(spir.x, spir.y, spir.z)
        pylab.draw()


def textSubmited(text):
        spir.deg = int(text)


def main():


        P = [[3, 0, 6],
             [0, 8, 0],
             [-10, 0, 3]]

        
        answer = GetBernPoly(P)

        u = sympy.Symbol('u')
        v = sympy.Symbol('v')
        mpl.rcParams['legend.fontsize'] = 10
        global fig, ax
        fig, ax = pylab.subplots()
        ax = fig.gca(projection='3d')


        axes_button_add = pylab.axes([0.7, 0.05, 0.25, 0.075])

        button_add = Button(axes_button_add, 'Вращать!')
        button_add.on_clicked(addButtonClicked)




        axbox = pylab.axes([0.85, 0.15, 0.1, 0.1])

        d1 = np.arange(0, 1, 0.01)
        d2 = np.arange(0, 1, 0.01)
        X, Y = np.meshgrid(d1, d2)
        a =[1.0]
        a = 100 * a
        Z = np.array(10*[a, a, a, a, a, a, a, a, a, a])

        for i in range(100):
                for j in range(100):
                        Z[i][j] =  answer.subs(u, d1[i]).subs(v, d2[j])

        ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
        ax.legend()
        pylab.show()



if __name__ == "__main__":
        main()


