import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)

# ==============================================================
# Defines the plotting function for the rest of the notebook.
#
def simplegraph(func,left=-25,right=25,samp1=90,samp2=110):
    x = np.linspace(left,right,samp1)
    y = func(x)
    yp = None
    xi = np.linspace(left,right,samp2)
    yi = np.interp(xi, x, y, yp)
    
    fig, ax = plt.subplots(figsize=(6,6))
    ax.grid(color='gray', linestyle=':', linewidth=0.5)
    ax.plot(x, y, 'o', xi, yi, '.')
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    plt.show()