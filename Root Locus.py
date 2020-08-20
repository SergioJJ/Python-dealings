"""
General Layout of this code

Transfer Function function
Compute Roots function
Plot Root Locus function
Main funciton

1st code sourced from
https://github.com/kevinzakka/root-locus/blob/master/root_locus.py
"""
from numpy.lib.scimath import sqrt
import numpy as np 
import matplotlib.pyplot as plot 
import seaborn as sea 
import control as cnt #used for second realization. requires installation



def transfer_function(num, denum):
    """
    "pads" the list of poles and zeros for representation of the 
    Transfer function
    
    Assume num is smaller than denum
    
    Parameters:
    -------
    - num: coeff of zeros [coeff_n, coeff_(n-1)..., coeff_0]
    - denum: coeff fo poles: [coeff_n, coeff_(n-1), .., coeff_0]
    
    Returns:
    - tf: 2d numpy array [num, denom]
    
    """
    
    #cast as numpy arrays of type float
    num = np.array(num, dtype = np.float64)
    denum = np.array(denum, dtype = np.float64)
    
    #get size difference
    size = len(denum) - len(num)
    
    #create array of zeros to "pad" with 
    temp = np.zeros(size)
    
    #join 0 pad and numerator
    num = np.concatenate((temp, num))
    
    #stack num and denum to create overall tf representation 
    tf = np.vstack((num, denum))
    return tf #end function 

def compute_roots(tf,gains):
    """
    Computes the roots of the characteristic equation of the closed loop system
    of a given transfer function for a list of gain parameters.
    
    Concretely, given TR = zeros/poles, and a gain value K, we solve for the 
    characteristic equation roots, that is the roots of poles + (K*zeros)

    Parameters:
    tf: 2D array
    gain: list of gains
    
    Returns:
    - roots: numpy array containing the roots for each gain in gains.
    """
    
    num, denum = tf[0], tf[1]
    num_roots = len(np.roots(denum))
    roots = []

    for gain in gains:
        ch_eq = denum + gain*num
        ch_roots = np.roots(ch_eq)
        ch_roots.sort()
        roots.append(ch_roots)
    
    #convert final roots list into array
    roots = np.stack(roots)
    return roots #end function


def plot_root_locus(gains, roots):
    """
    PLots the root locus of the closed loop system given the provided gains.
    
    Paramteres:
        gains
        roots
    
    returns:
        figure
        axis
    """
    #get real and imaginary value
    real_vals = np.real(roots)
    imag_vals = np.imag(roots)

    #colors to be used in the plot
    colors = ['b', 'm', 'c', 'r', 'g']

    #create figure and axis labels
    fig, ax = plot.subplots()
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.axvline(x = 0, color = 'k', lw = 1)
    ax.grid(True, which = 'both')
    
    #plots a blue "x" for the first roots
    ax.scatter(real_vals[0, :], imag_vals[0, :], marker = 'x', color = 'blue')

    ax.scatter(real_vals[-1, :], imag_vals[-1, :], marker = 'o', color = 'red')
    
    gain_text = ['k = {:1.2f}'.format(k) for k in gains]
    
    temp_real_vals = real_vals[1:-1, :]
    temp_imag_vals = imag_vals[1:-1, :]
    color_range = range(temp_real_vals.shape[1])
    
    #plot the rest of the roots in different colors with respect to the regions
    for r, i, j in zip(temp_real_vals.T, temp_imag_vals.T, color_range):
        ax.plot(r, i, color = colors[j])

    return fig, ax #end function

if __name__ == "__main__":
    #open loop transfer function
    num = [1,]
    denum = [1, 3.50,8]
    k = 516.666
    GH = k*transfer_function(num, denum)
    
    #create a list of evenly spaced gains
    gains = np.linspace(-0.5, 10.0, num = 2000)
    
    roots = compute_roots(GH, gains)
    fig, ax = plot_root_locus(gains, roots)    
 #   plot.show()
    
    """  This is the end of the first code and beginning of the second
2nd code requires installation of control library. Must run Anaconda command 
promt and enter this command:
    conda install -c conda-forge control
Root locus function discription here
https://python-control.readthedocs.io/en/0.8.2
/generated/control.matlab.rlocus.html#control.matlab.rlocus

To set the 
    
    """
    G = k*cnt.tf(num, denum)
    y = 5
    x = -5, 2
    cnt.rlocus(G, kvect =  gains, xlim = x, ylim = [-y, y], grid = True)



