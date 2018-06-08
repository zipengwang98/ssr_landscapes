import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib
from scipy import integrate
from scipy.integrate import odeint

#definition
mu_a = 1
mu_b = 1
m_aa = -1
m_bb = -1
m_ab = -0.5
m_ba = -0.5

mu = np.array([mu_a,mu_b])
M = np.array([[m_aa,m_ab],[m_ba,m_bb]])



def logi(z,t,mu,M):
    x,y = z
    Y = np.array([x,y])
    dzdt = np.dot(np.diag(mu), Y)+np.dot(np.diag(np.dot(M,Y)), Y)
    return dzdt


x0 = [0.1,0.9]
t = np.linspace(0,50,100000)

sol = odeint(logi, x0, t, args=(mu,M),mxstep=50000)
plt.plot(t, sol[:, 0], 'g', label='x(t)')
plt.plot(t, sol[:, 1], 'r', label='y(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('(Mxy,Myx) = (1.5,1.5),(x0,y0) = (.1,.9)')
plt.grid()
plt.show()