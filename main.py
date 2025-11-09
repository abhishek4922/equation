import pandas as pd
import numpy as np
from src.config import Config
from src.optimizer import global_initialization, alternating_optimization
from src.model import model_xy
from src.visualization import plot_fit
from src.utils import save_results
from src.equation_writer import save_final_equation  # ✅ NEW IMPORT

def main():
    # Load data
    df = pd.read_csv('data/xy_data.csv')
    x_obs, y_obs = df['x'].to_numpy(), df['y'].to_numpy()

    # Config
    cfg = Config()

    # Step 1: Coarse global search
    theta0, M0, X0 = global_initialization(x_obs, y_obs, cfg)

    # Step 2: Alternating optimization
    theta, M, X, t_final = alternating_optimization(x_obs, y_obs, theta0, M0, X0, cfg)

    # Step 3: Evaluate final model
    x_pred, y_pred = model_xy(theta, M, X, t_final)
    residuals = np.sqrt((x_pred - x_obs)**2 + (y_pred - y_obs)**2)

    print("\n[Final Results]")
    print(f" Theta = {np.rad2deg(theta):.4f}°")
    print(f" M = {M:.6f}")
    print(f" X = {X:.6f}")
    print(" Mean residual distance:", residuals.mean())

    # Save outputs
    save_results(x_obs, y_obs, t_final, theta, M, X)
    plot_fit(x_obs, y_obs, x_pred, y_pred, save_path='outputs/figures/final_fit.png')

    # Step 4: Save final equation
    save_final_equation(theta, M, X)

if __name__ == "__main__":
    main()
