import numpy as np
from math import cos


def precompute_logp_and_grad_function(
        char_exponent, skew=1, scale=None, loc=0,
        transform_width=100., transform_dt=.001):

    if scale is None:
        scale = cos(char_exponent * np.pi / 2) ** (1 / char_exponent)

    pdf, x = fourier_transform(
        lambda t: characteristic_func(t, char_exponent, skew, scale, loc),
        transform_width, transform_dt
    )
    pdf = np.real(pdf)
    grad, x = fourier_transform(
        lambda t: - complex(0, 1) * t * characteristic_func(t, char_exponent, skew, scale, loc),
        transform_width, transform_dt
    )
    grad = np.real(grad)

    logp = np.log(pdf)
    logp_grad = grad / pdf

    return x, logp, logp_grad


def characteristic_func(t, char_exponent, skew, scale, loc):
    if char_exponent == 1:
        raise NotImplementedError()
    return np.exp(
        complex(0, 1) * t * loc - np.abs(scale * t) ** char_exponent * (
            1 - complex(0, 1) * skew * np.sign(t) * np.tan(np.pi * char_exponent / 2)
        )
    )


def fourier_transform(f, integration_width, dt):
    """
    Parameters
    ----------
    f : vectorized function
    """
    t = np.arange(-integration_width, integration_width, dt)
    f_vector = f(t)
    g = np.fft.fft(f_vector)

    # Frequency normalization
    freq = np.fft.fftfreq(f_vector.size) * 2 * np.pi / dt

    # Multiply by a phase factor to get a discretisation of the continuous Fourier transform.
    g *= dt * np.exp(complex(0, 1) * freq * integration_width) / 2 / np.pi

    permutation = np.argsort(freq)
    freq = freq[permutation]
    g = g[permutation]

    return g, freq

