import numpy as np
import matplotlib.pyplot as plt
from mne.viz import plot_topomap
import scipy

def topoPlotIndie(eeg, values, ax, title='Topoplot', vlim=(None, None), cmap='jet', contours=6):
    def pol2cart(theta, rho):
        theta_rad = np.deg2rad(theta)
        x = rho * np.cos(theta_rad)
        y = rho * np.sin(theta_rad)
        return x, y

    head_rad = 0.095
    plot_rad = 0.51
    squeezefac = head_rad / plot_rad

    eeg_chanlocs = []
    for i in range(64):
        local_chanloc = []
        x = list(eeg['chanlocs'][0][0][0][i])
        th = x[1][0][0]
        rd = x[2][0][0]

        th, rd = pol2cart(th, rd)
        eeg_chanlocs.append([rd * squeezefac, th * squeezefac])

    eeg_chanlocs = np.array(eeg_chanlocs)

    im, _ = plot_topomap(values, eeg_chanlocs, axes=ax, show=False, 
                         cmap=cmap, contours=contours, vlim=vlim)
    ax.set_title(title)
 

