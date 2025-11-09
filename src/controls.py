import numpy as np
from scipy.interpolate import interp1d

def control_to_t(control, t_min, t_max, n):
    """Convert control deltas to a smooth time array t."""
    control_pos = np.abs(control) + 1e-8
    cum = np.cumsum(control_pos)
    cum_norm = (cum - cum[0]) / (cum[-1] - cum[0] + 1e-12)
    t_control = t_min + cum_norm * (t_max - t_min)

    xp = np.linspace(0, 1, len(control))
    f = interp1d(xp, t_control, kind='linear', fill_value='extrapolate')
    xi = np.linspace(0, 1, n)
    return f(xi)
