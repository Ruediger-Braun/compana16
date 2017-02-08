import numpy as np
from scipy.spatial import Delaunay 
from mayavi import mlab
import sympy
sympy.init_printing()
from IPython.display import display

def test_triangular_mesh(cmap):
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 80
    t = np.linspace(-np.pi, np.pi, n)
    z = np.exp(1j * t)
    x = z.real.copy()
    y = z.imag.copy()
    z = np.zeros_like(x)

    triangles = [(0, i, i + 1) for i in range(1, n)]
    x = np.r_[0, x]
    y = np.r_[0, y]
    z = np.r_[1, z]
    t = np.r_[0, t]

    return mlab.triangular_mesh(x, y, z, triangles, scalars=t, colormap=cmap)

def plot_rational_curve():
    r = np.linspace(0, 2, 100)
    phi = np.linspace(0, 2*np.pi, 400)
    R, Phi = np.meshgrid(r, phi)
    Z = R*np.exp(1j*Phi)
    V = Z / (1+Z**4)
    W = abs(V)
    B = W < 4
    Rf = R[B].flatten()
    Phi_f = Phi[B].flatten()
    Zf = Z[B].flatten()
    Xf = Zf.real
    Yf = Zf.imag
    Vf = V[B].flatten()
    Wf = abs(Vf)
    Theta_f = np.angle(Vf)
    dreiecke = Delaunay(np.array([Rf, Phi_f]).T)
    mlab.triangular_mesh(Xf, Yf, Wf, dreiecke.simplices,
                         scalars=Theta_f, colormap='hsv')


def plot_moebiusband():
    t = sympy.Symbol('t')
    s = sympy.Symbol('s')
    M = sympy.Matrix([ 3*sympy.cos(t) + s*sympy.sin(t/2),
                       3*sympy.sin(t),
                       s*sympy.cos(t/2)])
    sn = np.linspace(-1, 1)
    tn = np.linspace(0, 2*np.pi)
    S1, T1 = np.meshgrid(sn, tn)
    Sn, Tn = S1.T, T1.T
    fn = [sympy.lambdify((s,t), M[j], 'numpy') for j in range(3)]
    Xn = [fn[j](Sn, Tn) for j in range(3)]
    mlab.mesh(Xn[0], Xn[1], Xn[2], color=(1,0,0))
    return M
    

def plot_normale(M):
    s = sympy.Symbol('s')
    t = sympy.Symbol('t')
    seele = M.subs(s, 0)
    Mt = seele.diff(t)
    Ms = M.diff(s)
    display(Mt, Ms)
    N = Mt.cross(Ms)
    display(N)
    N_ein = seele + s*N/N.norm()
    sn = np.linspace(0.05, 1)
    tn = np.linspace(0, 2*np.pi)
    S1, T1 = np.meshgrid(sn, tn)
    Sn, Tn = S1.T, T1.T
    Nn = [sympy.lambdify((s,t), N_ein[j], 'numpy') for j in range(3)]
    Xn = [Nn[j](Sn, Tn) for j in range(3)]
    mlab.mesh(Xn[0], Xn[1], Xn[2], color=(1,.8,0))
