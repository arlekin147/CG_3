import numpy as np
import sympy

def polypow(poly, pow:int):
    if pow == 0: return 1
    answer = poly
    for num in range(1, pow):
        answer = sympy.S(answer)*sympy.S(poly)
    return answer


def binomial(n:int, k:int):
    return np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k)

def bezyeKoef(n , k, sym):
    sym = sympy.Symbol(sym)
    tk = np.zeros(k + 1)
    tk[0] = 1
    return binomial(n, k) * polypow(sym, k) * polypow(1 - sym, n - k )


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def GetBernPoly(P):
    n = len(P)
    m = len(P[0])
    z = 0
    for i in range(0, n, 1):
        temp = []
        for j in range(0, m, 1):
            koefX = (bezyeKoef(n, i, 'u'))
            koefY = (bezyeKoef(m, j, 'v'))
            z += P[i][j] * koefX * koefY
    return z

    








def main():
    lineX = [[1, 1], [2, 2], [3, 3]]
    lineY = [[1, 1], [2, 2], [3, 3]]
    P = [[Point(0, 0, 0), Point(0, 1, 0)], [Point(1, 0, 0), Point(1, 1, 2)], [Point(2, 0, 1),
     Point(2, 0, 3)], [Point(3, 0, 1), Point(3, 1, 6)]]
    print("OGO:") # P[0][0] - Z P
    print(P[0][0].x)
    answer = GetBernPoly(P)

    mpl.rcParams['legend.fontsize'] = 10
    global fig, ax
    fig, ax = pylab.subplots()
    ax = fig.gca(projection='3d')
    ax.plot(answer[0], answer[1], answer[2], label='parametric curve')
    ax.legend()

    print(polypow([1, 1], 1))


if __name__ == "__main__":
    main()