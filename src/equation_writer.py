# src/equation_writer.py
"""
equation_writer.py
------------------
Writes the final optimized parametric equations x(t) and y(t)
to a readable text file.
"""

import numpy as np
import os

def save_final_equation(theta, M, X, output_dir="outputs/equations", filename="final_equation.txt"):
    """
    Save the final optimized model equations x(t) and y(t) using the optimized parameters.

    Parameters
    ----------
    theta : float
        Rotation angle in radians.
    M : float
        Exponential coefficient.
    X : float
        X offset.
    output_dir : str
        Directory where the equation file will be saved.
    filename : str
        Output filename.
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    theta_deg = np.rad2deg(theta)

    eq_x = (
        f"x(t) = t * cos({theta:.6f}) "
        f"- exp({M:.6f} * |t|) * sin(0.3*t) * sin({theta:.6f}) + {X:.6f}"
    )
    eq_y = (
        f"y(t) = 42.0 + t * sin({theta:.6f}) "
        f"+ exp({M:.6f} * |t|) * sin(0.3*t) * cos({theta:.6f})"
    )

    text = (
        "Final Optimized Model Equations\n"
        "--------------------------------\n"
        f"Theta (deg): {theta_deg:.6f}\n"
        f"M: {M:.6f}\n"
        f"X: {X:.6f}\n\n"
        f"{eq_x}\n"
        f"{eq_y}\n"
    )

    with open(filepath, "w") as f:
        f.write(text)

    print(f"\n Final equations saved to '{filepath}'")
