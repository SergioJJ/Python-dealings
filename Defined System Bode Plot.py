"""
Sergio Jimenez
Linear Control Systems 
Python Assignment #1
Bode Plot Magnitude and Phase plotter
with corresponding table

"""
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

#constants
pi = 3.14159
start_freq = 1  
stop_freq = 1E9 
#arrays needed
pole_mag = []
pole_phase = []
zero_mag = []
zero_phase = []

print ("\nBode Plotter Program")
print ("written by Sergio Jimenez\n")
print ("This system will have 3 poles and 2 zeros.")
print ("Please enter each value's respective magnitude and phase one at a time.\n") 

while True:
    
    for poles in range(1, 4):
        print ("Please input pole #", poles, " magnitude: ")
        value = float(input(poles))
        pole_mag.append(value)
        value = float(input("and the phase: "))
        pole_phase.append(value)

    for zeros in range(1, 3):
        print ("Please input zero #", zeros, " magnitude: ")
        value = float(input(zeros))
        zero_mag.append(value)
        value = float(input("and the phase: "))
        zero_phase.append(value)
    print("\nGenerating Table and Bode plot graphs...\n")

    #test case used for Tsing
#-50    pole_mag = [0, -10000, -100000]
  #  pole_phase = [50, -90, 45]
  #  zero_mag = [-1000, -10000]
  #  zero_phase = [0, -90]



    z1 = complex(zero_mag[0], zero_phase[0])
    z2 = complex(zero_mag[1], zero_phase[1])
    p1 = complex(pole_mag[0], pole_phase[0])
    p2 = complex(pole_mag[1], pole_phase[1])
    p3 = complex(pole_mag[2], pole_phase[2])

    s = np.logspace(np.log10(start_freq), np.log10(stop_freq), num = 1000  , dtype = float) #need to find what 'axis' equi  #temporal change to linspace, to test 
    k = 25*(z1*z2)/(p1*p2*p3) # as K is represendted with this math
    N = (1-(s/z1))*(1-(s/z2))
    D = (1-(s/p1))*(1-(s/p2))*(1-(s/p3))
    G = (N/D)

    magnitude = 20*np.log10(abs(G))
    phase = np.angle(G)*180/pi


    plot.figure(figsize = [12,3])
    plot.subplot(121)
    plot.semilogx(s, magnitude)  
    plot.grid(True, which = 'both')
    plot.xscale('log')
    plot.ylabel("Magnitude (dB)")
    plot.xlabel("Radian Frequency (rad/sec)")
    
    p = plot.subplot(122)
    plot.semilogx(s, phase)
    p.yaxis.set_label_position("right")
    plot.ylabel("Phase (Degrees)")
    plot.xlabel("Radian Frequency (rad/sec)")
    plot.grid(True, which = 'both')
    
    ##rerun this calculation with less data points to get proper indexing at the table
    s = np.logspace(np.log10(start_freq), np.log10(stop_freq), num = 10  , dtype = float)
    N = (1-(s/z1))*(1-(s/z2))
    D = (1-(s/p1))*(1-(s/p2))*(1-(s/p3))
    G = (N/D)
    magnitude = 20*np.log10(abs(G))
    phase = np.angle(G)*180/pi

    table = pd.DataFrame({'Frequency' : s, 'Magnitude' : magnitude, 'Phase' : phase})
    #table_values, columns = ['Frequency', 'Magitude', 'Phase'] )
    table.set_index('Frequency') 
    print(table)

    play_again = input("Play Again? (y/n)").lower()
    if play_again[0] != "y":
        break
"""
while True:
     tries = GuessUntilCorrect(27) #probably want to use a random number here
     print("It Took %d Tries For the right answer!"%tries)
     play_again = input("Play Again?").lower()
     if play_again[0] != "y":
        break
"""
