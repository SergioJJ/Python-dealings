# author: Sergio Jimenez
#
# Python script to compute the discrete Fourier transform of a signal using scipy, as guided by online examples at:
# https://hub.packtpub.com/compute-discrete-fourier-transform-dft-using-scipy/ 
# and 
# https://www.asee.org/file_server/papers/attachment/file/0005/4418/Eric_-Javad-_Muqri_Final_version__-_A_Taste_of_Python-_DFT_and_FFT.pdf
# 
# 
# The progam currently either reads in a csv file with signal data modeled as (step, value)
# or uses one sample signal to generate the graphs. This signal can be manipulated by changing the 
# values present in amplitude and frequency
#
# The program plots the input signal and output of the fft 
#
# main function to be used in this script:
# fft(x[, n, axis, overwrite_x])


import numpy as np
import pandas as pd
from scipy.fftpack import fft 
#from scipy import signal as sig  # will add square wave function later
import matplotlib.pyplot as plt

# bank of signal parameters
# edit these values to change the signals genrated. can be expanded or reduced
amplitude = [1.0,   0.8,    0.4,    1.0,    0.8,    0.6]
freq    =   [50,    80,     306,    600,    45,     133]



print("Welcome to the FFT machine! You can select from a small collection of signals, or import your own")
usersignal = input("Would you like to import your own signal? [Y/N]").lower()

if usersignal[0] == 'y':                # corresponds to accepting to input user data
    
    TIMEINDEX = pd.read_csv("DATA.csv", dtype = str, usecols = [0])
    SIGNAL = pd.read_csv("DATA.csv", dtype = np.float64,usecols = [1])

    n_length = TIMEINDEX.shape[0]
    n = n_length  ## placeholder until user choice is implemented

    x = np.linspace(0.0, n, n)
    y = SIGNAL             # append signal to graphing
    print("Your signal has ", n_length, " entries")

    sample_freq = input("What is the frequency at which the samples were taken? ")
    t = 1/float(sample_freq)


if usersignal[0] != 'y':
    #integer n indicates the length of the transform
    print("Generating signal from parameter listing...")
    n = 2.1*max(freq)                   # 2.1 ensures the niquist frequency for sampling is met
    t = 1/(n)                           # constant used for spacing time and frequency domains
    x = np.linspace(0.0, n*t, n)        # creates a linear space for our signals to live in

    SIGNAL = []
    for i, f in enumerate(freq):
        SIGNAL.append(amplitude[i]*np.sin(2*np.pi*f*x))
    y = np.sum(np.array(SIGNAL), axis = 0)


yf = fft(y)                             # execute the fourier transform


Y = 2.0/n * np.abs(yf[0:int(n/2)])      #setup for the frequency domain graphing
X = np.linspace(0.0, 1.0/(2.0*t), n//2)

PLOT_SIZE = (15,10)
DPI = 300

fig1 = plt.figure(figsize = PLOT_SIZE)
fig1.suptitle('The input signal in the time domain')
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
if usersignal[0] == 'y':
    plt.savefig('usergraph_input.PNG', dpi = DPI)
else:
    plt.savefig('generatedgraph_input.PNG', dpi = DPI)
plt.show()
fig2 = plt.figure(figsize = PLOT_SIZE)
fig2.suptitle('The FFT of the signal in the frequency domain')
plt.plot(X,Y)
plt.xlabel('Frequency - (Hz)')
plt.ylabel('Amplitude')
plt.grid()
if usersignal[0] == 'y':
    plt.savefig('usergraph_fft.PNG', dpi = DPI)
else:
    plt.savefig('generatedgraph_fft.PNG', dpi = DPI)
plt.show()


