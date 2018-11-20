from IPython.display import display
from scipy import signal
import sympy as sy
import matplotlib.pyplot as plt


sy.init_printing()  # LaTeX like pretty printing for IPython

def lti_to_sympy(lsys, symplify=True):
    """ Convert Scipy's LTI instance to Sympy expression """
    s = sy.Symbol('s')
    G = sy.Poly(lsys.num, s) / sy.Poly(lsys.den, s)
    return sy.simplify(G) if symplify else G


def sympy_to_lti(xpr, s=sy.Symbol('s')):
    """ Convert Sympy transfer function polynomial to Scipy LTI """
    num, den = sy.simplify(xpr).as_numer_denom()  # expressions
    p_num_den = sy.poly(num, s), sy.poly(den, s)  # polynomials
    c_num_den = [sy.expand(p).all_coeffs() for p in p_num_den]  # coefficients
    l_num, l_den = [sy.lambdify((), c)() for c in c_num_den]  # convert to floats
    return signal.lti(l_num, l_den)

def multiply(s1,s2):
    s1,s2=lti_to_sympy(s1),lti_to_sympy(s2)
    r=sy.simplify(s1*s2).expand()
    display(sy.Eq(Hs, r))
    lti_r=sympy_to_lti(r)
    return lti_r

Hs = sy.symbols("H(s)")  # only needed for displaying

# Sample systems:
lti_G = signal.lti([1], [6.3354e-8, 7.1227e-5,1])
lti_H = signal.lti([1], [ 8.8952e-4, 1])

r = multiply(lti_G,lti_H)

w,mag,phase = signal.bode(r,1000)
plt.figure()
plt.semilogx(w,mag)

