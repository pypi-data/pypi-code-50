import numpy as np
import matplotlib.pyplot as plt


def fourier_transform(f, t_width, dt):
    """
    Parameters
    ----------
    f : vectorized function
    t_range : array of length 2, integration range
    dt : float
    """
    t = np.linspace(-t_width, t_width, dt)
    g = np.fft.fft(f)

    # Frequency normalization
    w = np.fft.fftfreq(f.size) * 2 * np.pi / dt

    # Multiply by a phase factor to get a discretisation of the continuous Fourier transform.
    g *= dt * np.exp(complex(0, 1) * w * t_width) / (np.sqrt(2 * np.pi))

    return g


#Discretize time t
t0 = -100.
dt = 0.001
t = np.arange(t0, -t0, dt)
#Define function
f=1./(t** 2+1.)

#Compute Fourier transform by numpy's FFT function
g=np.fft.fft(f)
#frequency normalization factor is 2*np.pi/dt
w = np.fft.fftfreq(f.size)*2*np.pi/dt


#In order to get a discretisation of the continuous Fourier transform
#we need to multiply g by a phase factor
g*=dt*np.exp(-complex(0,1)*w*t0)/(np.sqrt(2*np.pi))

#Plot Result
plt.scatter(w, g, color="r")
#For comparison we plot the analytical solution
plt.plot(w, np.exp(-np.abs(w)) * np.sqrt(np.pi / 2), color="g")

plt.gca().set_xlim(-10, 10)
plt.show()
plt.close()