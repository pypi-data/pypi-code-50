"""
Input encoding
"""
import inspect
import numpy as np
import scipy.signal as signal
import copy

from .utils import get_default_kwargs

"""
Shapes of signals

(time,) -> (time, 1)
1D arrays are 1D signals

(time, D)
2D arrays are D-dimensional signals
With D=2 we have a vector signal

(time, H, W)
3D arrays are signals on a WxH grid

(time, H, W, D)
4D arrays are D-dimensional signals on a WxH grid
With D=2 we have a vector signal on a grid

In general signals can take any shape as part of the encoding process.
However, the last step must produce an output of either
(time, 2): a global vector signal
(time, H, W, 2): a local vector signal on a grid

"""
class Encoder:
    def __init__(self, *steps, verbose=False):
        self.steps = steps
        self.params = [self._get_default_params(s) for s in steps]
        self.verbose = verbose

    def _verbose(self, *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)

    def encode(self, input, verbose=False):
        """ Encode input stream

        input.shape = (n_inputs, input_dim)
        output.shape = (n_inputs, time, output_dim, ...) # step
                     = (n_inputs, time, 2)               # global field
                     = (n_inputs, time, height, width)   # local field on grid
        """
        input = np.array(input)
        self._verbose(f'input {input.shape}', end=' ')
        for step, params in zip(self.steps, self.params):
            input = step(input, **params)
            self._verbose(f'-> {step.__name__}({params})', end=' ')
            self._verbose(f'-> {input.shape}', end=' ')
        self._verbose('')
        return input

    def __call__(self, input):
        return self.encode(input)

    @staticmethod
    def _get_default_params(step):
        return dict(get_default_kwargs(step))

    def get_default_params(self):
        params = {}
        for p in self.get_params():
            params.update(p)
        return params

    def get_params(self):
        return self.params

    def set_param(self, name, value):
        """ Set all params matching name """
        for param in self.params:
            if name in param:
                param[name] = value

    def set_params(self, **params):
        for k, v in params.items():
            self.set_param(k, v)

    def __repr__(self):
        return f'Encoder({self.steps})'

def expand_dims(input):
    """ Add a new dimension at the end """
    return np.expand_dims(input, -1)

def check_input(input):
    input = np.array(input)
    if len(input.shape) == 1:
        return expand_dims(input)
    return input

def squeeze(input):
    """ Squeeze all but the first axis """
    time = input.shape[0]
    input_shape = input.shape[1:]
    input_shape = tuple(dim for dim in input_shape if dim > 1)
    return input.reshape((time,) + input_shape)

# Steps as simple functions
def scale(input, H0=0, H=1):
    """ Scale input to range [H0, H] """
    return H0 + input * (H - H0)

def angle(input, phi0=0, phi=360):
    """ Map input to angle in range [phi0, phi] -> vector components """
    input = check_input(input)
    theta0 = np.deg2rad(phi0)
    theta = np.deg2rad(phi)
    angles = theta0 + input * (theta - theta0)
    # add one dimension for vector
    out = expand_dims(angles)
    out = np.repeat(out, 2, axis=-1)
    out[...,0] = np.cos(out[...,0])
    out[...,1] = np.sin(out[...,1])
    return squeeze(out)

def angle_grid(input, phi0=0, phi=360, grid=None):
    """ Convenience function to offset all angles based on grid """
    input = expand_dims(check_input(input))
    if grid is not None:
        phi0 = grid + phi0
        phi = phi0 + phi
    return angle(input, phi0, phi)


def sw(input, rotation=0):
    """ Multiply input vectors by SW astroid """
    input = check_input(input)
    angles = np.arctan2(input[...,1], input[...,0])
    angles = angles - np.deg2rad(rotation)

    Hs = (np.abs(np.sin(angles))**(2/3) + np.abs(np.cos(angles))**(2/3))**(-3/2)
    Hs.shape += (1,)

    return Hs * input

def broadcast_waveform(input, waveform):
    """ Broadcast waveform over input """
    input = check_input(input)
    # multiply input by waveform (broadcasting rules apply)
    out = input * waveform
    # roll last axis to the first (time)
    out = np.moveaxis(out, -1, 1)
    # finally concatenate it
    out = np.concatenate(out)
    return squeeze(out)

def sin(input, timesteps=100):
    """ Multiply input by sine wave """
    t = np.linspace(0, 2 * np.pi, timesteps, endpoint=False)
    waveform = np.sin(t)
    return broadcast_waveform(input, waveform)

def triangle(input, timesteps=100):
    """ Multiply input by triangle wave """
    t = np.linspace(np.pi/2, 2*np.pi + np.pi/2, timesteps, endpoint=False)
    waveform = signal.sawtooth(t, 0.5)
    return broadcast_waveform(input, waveform)

def rotate(input, timesteps=100):
    """ Multiply input by rotation vector """
    t = np.linspace(0, 2 * np.pi, timesteps, endpoint=False)
    cos = broadcast_waveform(input, np.cos(t))
    sin = broadcast_waveform(input, np.sin(t))
    return np.stack([cos, sin], axis=-1)

def ppm(input, pos0=0, pos=1.0, timesteps=100):
    """ Pulse position modulation """
    input = check_input(input)

    # output shape
    shape = input.shape + (timesteps,)

    # calculate location of pulses
    pulse_inds = scale(input, pos0 * timesteps, pos * (timesteps-1)).round().astype(int)
    inds = tuple(np.array(list(np.ndindex(shape[:-1]))).T)
    inds += (pulse_inds.flatten(),)

    # make the pulses
    out = signal.unit_impulse(shape, inds)

    return squeeze(out)

def fixed_vector(input, phi=0):
    """ Convert scalar input to vectors at some angle phi """
    input = check_input(input)
    theta = np.deg2rad(phi)
    # add one dimension to broadcast vector
    input = expand_dims(input)
    vector = [np.cos(theta), np.sin(theta)]
    out = input * vector
    return squeeze(out)

def rotate_vector(input, phi=0):
    """ Rotate vector input by some angle phi """
    input = check_input(input)
    input_shape = input.shape
    theta = np.deg2rad(phi)
    rotation_matrix = np.array(
        [[np.cos(theta), -np.sin(theta)],
         [np.sin(theta),  np.cos(theta)]])
    input = input.reshape((-1,2)).T
    out = np.dot(rotation_matrix, input).T
    out = out.reshape(input_shape)
    return squeeze(out)

def ensure2d(input, fill=1.0):
    """ Convert scalar input to vectors """
    input = check_input(input)
    if input.shape[-1] == 1:
        input = np.column_stack([input, np.full(len(input), fill)])
    return input

def grid(input, grid_size=(3,3), grid=None):
    """ Encode input onto grid

    Parameters
    ----------
    grid_size : tuple
        Create grid of fixed size (uniform weights)
        Ignored if grid is set
    grid : array
        Create grid of given size (non-uniform weights)
    """
    if grid is None:
        w, h = grid_size
        grid = np.ones((h, w))
    else:
        grid = np.atleast_2d(grid)

    input = check_input(input)

    # add dimensions to broadcast the grid
    input = input.reshape(input.shape + (1,) * grid.ndim)

    # broadcast the grid on each feature
    out = grid * input

    # now we have:
    # out.shape = (time,) + input.shape + grid.shape
    # shift axes to the end until we have the desired:
    # out.shape = (time,) + grid.shape + input.shape
    for i in range(out.ndim - grid.ndim - 1):
        out = np.moveaxis(out, 1, -1)

    return squeeze(out)

def onehot(input, nbits=2):
    input = check_input(input)

    # roll bit string 00..01 according to input
    out = np.zeros(input.shape + (nbits,))
    out[...,0] = 1
    for i, v in np.ndenumerate(input.astype(int)):
        out[i] = np.roll(out[i], v)

    # roll last axis to the first (time)
    out = np.moveaxis(out, -1, 1)

    # finally concatenate it
    out = np.concatenate(out)

    return squeeze(out)

"""
Define some encoders
"""
encoders = {
    'constant': Encoder(scale, fixed_vector),
    'angle': Encoder(angle, scale),
    'sw-angle': Encoder(angle, sw, scale),
    'sin': Encoder(scale, sin, fixed_vector),
    'triangle': Encoder(scale, triangle, fixed_vector),
    'angle-sin': Encoder(angle, expand_dims, sin, scale),
    'angle-triangle': Encoder(angle, expand_dims, triangle, scale),
    'angle-sin-grid': Encoder(angle, expand_dims, sin, scale, grid), # grid determines H
    'angle-grid-sin': Encoder(angle_grid, expand_dims, sin, scale), # grid adds angle offset
    'rotate': Encoder(scale, rotate),
    'sw-rotate': Encoder(scale, rotate, sw),
    'rotate-pulse': Encoder(ppm, scale, rotate),
    'sw-pulse': Encoder(ppm, scale, rotate, sw),
    'triangle2d': Encoder(scale, ensure2d, triangle, rotate_vector),
    'onehot': Encoder(onehot, scale, triangle, fixed_vector),
    'constant-grid': Encoder(grid, scale, fixed_vector),
    'sin-grid': Encoder(grid, scale, expand_dims, sin, fixed_vector),
    'triangle-grid': Encoder(grid, scale, expand_dims, triangle, fixed_vector),
    'rotate-pulse-grid': Encoder(ppm, grid, scale, rotate),
    'sw-pulse-grid': Encoder(ppm, grid, scale, rotate, sw),
    'direct': Encoder(scale),
}

def get_encoder(name, **params):
    encoder = copy.deepcopy(encoders[name])
    encoder.set_params(**params)
    return encoder

if __name__ == '__main__':
    SinEncoder = Encoder(scale, sin, fixed_vector)
    SinEncoder.set_params(vmin=0.5, vmax=1.0, timesteps=100)

    print('SinEncoder params:', SinEncoder.get_params())

    SinGridEncoder = Encoder(grid, scale, sin, fixed_vector)
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    SinGridEncoder.set_params(H0=0.5, H=1.0, grid=grid, timesteps=100, phi=10)

    print('SinGridEncoder params:', SinGridEncoder.get_params())

    input = np.array([[1,0,0]]).T
    print('input=', input)

    # SinEncoder.verbose = True
    # signal = SinEncoder(input)
    # print('signal=', signal)

    SinGridEncoder.verbose = True
    gsignal = SinGridEncoder(input)

    import matplotlib.pyplot as plt
    # plt.plot(signal)
    plt.subplot(211)
    for i in range(gsignal.shape[1]):
        for j in range(gsignal.shape[2]):
            plt.plot(gsignal[:,i,j,0], label=f'{i},{j}')
    plt.subplot(212)
    for i in range(gsignal.shape[1]):
        for j in range(gsignal.shape[2]):
            plt.plot(gsignal[:,i,j,1], label=f'{i},{j}')
    plt.legend()
    plt.show()
