# -*- coding: utf-8 -*-
"""
Emag Python Assignment #2
may also dump LCS code in here

****************************************************   8/19/2020
I know for a fact this spits out incorrect values
****************************************************

Determine if a material is a Lossless Medium, a Low-Loss Medium, a Good Conductor,
or in general Any Medium, and then
 Calculate the propagation parameters

Inputs
 Type of material by number (from the table)
 Frequency in Hz

Outputs
 Name of material you've selected (after you enter the number)
 Type of material (Lossless Medium, Low-Loss Medium, Good Conductor, or Any
Medium)
 After the type of medium is determined,
o  (Np/m),
o  (rad/m),
o c (ohms, polar),
o up (m/s),
o  (m)

Relevant equations: See table 7.1
Your code must
 Prompt the user for the material by number
 Show the material name after that number is entered
 Prompt the user for frequency in Hz
 Output the type of material (Good Conductor, etc)
 Output the propagation parameters , , c, up, 
 Ask the User whether
o Input another case? or
o Exit (gracefully!)
sergio
"""
import math
import cmath

u_0 = cmath.pi*4E-7
e_0 = 8.854E-12 #abs permittivity e_abs = e_0*e_r


print(""""
Sergio Jimenez
Emag Python Assignment #2

THE WAVE MEDIUM CHARACTERIZATION PROGRAM

      """)

dict = { #begin lookup table
1 : {'id': 'Fresh water'    ,'e_r':  80, 'row':   5E-4, 'u_r' :   1},
2 : {'id': 'Sea water'      ,'e_r':  80, 'row':      3, 'u_r' :   1},
3 : {'id': 'Ice'            ,'e_r': 3.5, 'row':   1E-5, 'u_r' :   1},
4 : {'id': 'Clay'           ,'e_r':  20, 'row':      5, 'u_r' :   1},
5 : {'id': 'Barium Titanate','e_r':3279, 'row':   1E-6, 'u_r' :   1},
6 : {'id': 'Pure Iron'      ,'e_r':   1, 'row':    1E7, 'u_r' : 5E3},
7 : {'id': 'Mu metal'       ,'e_r':   1, 'row':  1.6E6, 'u_r' : 2E5},
8 : {'id': 'Copper'         ,'e_r':   1, 'row': 5.96E7, 'u_r' :   1},
9 : {'id': 'Graphite'       ,'e_r':12.5, 'row':    2E5, 'u_r' :   1},
10: {'id': 'Diamond'        ,'e_r': 7.5, 'row':  1E-13, 'u_r' :   1},
11: {'id': 'Glass'          ,'e_r':  65, 'row':  1E-15, 'u_r' :   1},
12: {'id': 'PTFE'           ,'e_r': 2.1, 'row':  1E-25, 'u_r' :   1},
} #end of lookup table

while True:
#  {
#rint(" ")  #print table of values from dict, prbably a for loop
#user input and parameter definitions
    print("""
CHOOSE YOUR PLAYER!

1 FRESH WATER     2 SEA WATER     3 ICE ICE BABY     4 CLAY
5 BARIUM TITANATE 6 PURE IRON     7 MU METAL         8 COPPER 
9 GRAPHIE         10 DIAMOND      11 GLASS           12 PTFE
    """)
    material = int(input("WHAT IS YOUR CHOICE??? "))
    identity = dict[material]['id']
    e_r = dict[material]['e_r']
    row = dict[material]['row']
    u_r = dict[material]['u_r']


    print("\nYOU CHOSE: ", identity, "!!!")

    frequency = int(input("WHAT IS YOUR FREQUENCY(Hz)??? "))
    #end of user input

    #calculations
    rad_freq = 2*cmath.pi*frequency
    e_abs = e_0*e_r
    u_abs = u_r*u_0
    medium_qual = (row)/(rad_freq*e_abs)
    alpha = rad_freq*math.sqrt(((math.sqrt(1+medium_qual**2)-1)*(u_abs*e_r)/2))
    beta = rad_freq*math.sqrt(((math.sqrt(1+medium_qual**2)+1)*(u_abs*e_r)/2))
    wave_impedance = ((u_abs/e_abs)**(1/2))*complex(1,-medium_qual)**(-1/2)
    prop_vel = rad_freq/beta
    wavelength = 2*cmath.pi/beta

    #testing for material quality, may still have a few bugs present
    lossless = False
    if alpha == 0:
        quality = "is a Lossless Medium"
        lossless = True
    if medium_qual > 100 : 
        quality = "is a Good Conductor"
    if lossless == False:    
        if medium_qual < 0.01 :
            quality = "is a Low Loss Medium"


    if medium_qual < 100 :
        if medium_qual > 0.01 :
            quality = "has no particular conducting properties (Any Medium)"

    print("\n\nThis material " , quality, " at the chosen frequency.") 
    
    print("\nFor ", identity, "at ", frequency, "Hz"
          "\nPropagation speed is ", prop_vel,"m/s",
          "\nAlpha value is ", alpha, "Np/m",
          "\nBeta value is ", beta, "rad/m",
          "\nWave Impedance is ",cmath.polar(wave_impedance)," (Mag,Deg) ohms",
          "\nWavelength is ", wavelength, " m")

    play_again = input("FINISH!!\n\nWOULD YOU LIKE TO PLAY AGAIN??? (y/n)").lower()
    if play_again[0] == "y":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if play_again[0] != "y":
        break


