import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import os
import sys
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

# arguments for image file extension and r value
try:
    r = float(sys.argv[1])
    imgfile = sys.argv[2]
    dpi = int(sys.argv[3])
except Exception as e:
    print('input format: taucauto.py r imgfile dpi')
    print('r : tauc plot exponent value')
    print('imgfile : image file type/extension')
    print('dpi : image quality (dpi)')
    exit()

# Directory containing spectra to be analysed
dirname = '.'

# Function returning excitation energy
def GetHv(x):
    return (6.626070e-34*299792458)/(x*1e-9)*6.242e18

# Function returning Tauc plot y-axis (direct, allowed transitions)
def GetAlpha(hv,f,r):
    return (hv*f)**(1/r)

gaps = []
for spectrum_file in os.listdir(dirname):
    if spectrum_file.endswith('.txt'):
        with open(dirname+'/'+spectrum_file,'r') as input_file:
            spectrum = np.array([line.split() for line in input_file][2:]).astype(np.float)

        # Calculate Tauc plots
        tauc_spectrum = np.zeros((len(spectrum),2))
        tauc_spectrum[:,0] = GetHv(spectrum[:,0])
        tauc_spectrum[:,1] = GetAlpha(GetHv(spectrum[:,0]), spectrum[:,1], r)

        # Transform Tauc plot to interpolation function
        y = interp1d(tauc_spectrum[:,0], savgol_filter(tauc_spectrum[:,1], 51, 3))
        x = np.linspace(tauc_spectrum[0,0], tauc_spectrum[-1:,0], 5000)

        # Calculate 1st derivative along Tauc plot
        dy = np.diff(y(x), 1)
        dx = np.diff(x, 1)
        y_1d = interp1d(x[:-1], dy/dx)

        # Calculate 2nd derivative along Tauc plot
        d2y = np.diff(y(x), 2)
        dx2 = 0.0001
        y_2d = interp1d(x[:-2], d2y/dx2)

        # Find point in Tauc plot where 2nd derivative == 0 and gradient is at a maximum
        gradmax = 0.
        for i in range(2, len(x[:-2])):
            grad = y_1d(x[:-2])[i]
            if grad > gradmax:
                gradmax = grad
            if np.allclose([y_2d(x[:-2])[i]], [0.], atol=0.001) and y(x)[i] > 0.1*np.amax(tauc_spectrum[:,1]) and grad >= gradmax:
                x_0 = x[i]
                y_0 = y(x)[i]

        # Calculate extrapolation line
        m = y_1d(x_0)
        c = y_0 - m*x_0

        # Calculate optical gap from extrapolation line
        x_cross = (0 - c)/m
        gap = x_cross
        gaps.append([spectrum_file, x_cross])

        # Plot Tauc plot, extrapolation line and point equal to optical gap
        plt.xlabel(r'$ h \nu$ (eV)')
        plt.ylabel(r'$( \alpha h \nu )^{1/r}$ $(cm^{-1})$')
        plt.figtext(0.15, 0.8, 'Optical Gap = '+str(x_cross)[:4]+' eV')

        plt.plot(tauc_spectrum[:,0], tauc_spectrum[:,1],'-',
                 [(0-c)/m, (0.7*np.amax(tauc_spectrum[:,1])-c)/m], [0, 0.7*np.amax(tauc_spectrum[:,1])], '--',
                 tauc_spectrum[:,0], np.zeros(len(tauc_spectrum)), '-',
                 x_cross, 0, 'o', )

        plt.savefig(spectrum_file[:-4]+'.'+imgfile, dpi=dpi)
        plt.close()

with open('output.dat', 'w') as computed_gaps:
    computed_gaps.write('filename\tgap (eV) \n')
    for item in gaps:
        computed_gaps.write('{}\t{}\n'.format(item[0], item[1]))
