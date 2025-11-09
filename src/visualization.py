import matplotlib.pyplot as plt

def plot_fit(x_obs, y_obs, x_pred, y_pred, save_path=None):
    plt.figure(figsize=(7,7))
    plt.scatter(x_obs, y_obs, s=6, alpha=0.6, label='Observed')
    plt.plot(x_pred, y_pred, 'r-', lw=2, label='Fitted')
    plt.legend()
    plt.gca().set_aspect('equal', 'box')
    plt.title('Final Fit (with estimated t)')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
