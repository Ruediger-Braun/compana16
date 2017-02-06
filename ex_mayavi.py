
import numpy as np
from scipy.spatial import Delaunay 
from mayavi import mlab

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
    R1, Phi1 = np.meshgrid(r, phi)
    R, Phi = R1.T, Phi1.T
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

def plot_rational_curve2():  # works poorly 
    r = np.linspace(0, 2, 100)
    phi = np.linspace(0, 2*np.pi, 400)
    R1, Phi1 = np.meshgrid(r, phi)
    R, Phi = R1.T, Phi1.T
    Z = R*np.exp(1j*Phi)
    V = Z / (1+Z**4)
    W = abs(V)
    W[W>4] = np.nan
    Rf = R.flatten()
    Phi_f = Phi.flatten()
    Zf = Z.flatten()
    Xf = Zf.real
    Yf = Zf.imag
    Vf = V.flatten()
    Wf = W.flatten()
    Theta_f = np.angle(Vf)
    dreiecke = Delaunay(np.array([Rf, Phi_f]).T)
    mlab.triangular_mesh(Xf, Yf, Wf, dreiecke.simplices,
                         scalars=Theta_f, colormap='hsv')

