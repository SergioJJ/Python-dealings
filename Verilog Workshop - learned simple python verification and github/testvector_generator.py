# -*- coding: utf-8 -*-
"""
Python script to verify 16 bit adder using analysis provided by Dr. Aslan

@author: sergi0
"""

import numpy as np #import numpy lib
import pandas as pd
import matplotlib.pyplot as plt
n = int(input("Enter input bit size (default 16): ")) #ask user for for number of bits
N = int(input("Enter number of testvectors: "))  #ask user for the number of test vectors to be performed
k = int(input("Enter the number of inputs to generate (default  2): ")) #ask user for number of inputs to generate


test_vectors = np.uint32(2**n**np.random.rand(N,k)) # generate numpy array values (N,k)
#print(test_vectors)  # print test vectors (optional)

np.savetxt('in_vec.txt', test_vectors, delimiter = ' ', fmt = "%.4X")

input("Run the simulation and verify out_vec.txt generated, then press enter to continue")

AA = pd.read_csv("out_vec.txt", delimiter = ' ', header = None, skiprows = 2)

Values = AA.values # this will get the three column numpy array

arrayA = Values[:,0]  #A vaector values
arrayB = Values[:,1]  #B vector values
Out    = Values[:,2]  #output  values
N = np.arange(0,arrayA.size)  #determines number of testvectors tested
test = abs(arrayA+arrayB-Out); #will highlight any discrepancies
plt.plot(N,test)
plt.show()

#k = 0
#j = 0
#for i in (test):
#    if (i<1e-16):
#        #print("Passed")
#        k = k+1
#    else:
 #       j = j+1#
#
#print(f"Total number of testvectors \t: {len(test)}")
#print(f"Total number of Passes \t\t: {k}")
#print(f"Total number of Fails \t\t: {j}")
#print(f"Error {%} \t\t\t: %{100*j/(j+k)}")

