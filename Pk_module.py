#!/usr/bin/python
import sys
import numpy as np
from scipy.interpolate import interp1d


# README:
#
# This is an example python script for the external_Pk mode of Class.
# It generates the primordial spectrum of LambdaCDM.
# It can be edited and used directly, though keeping a copy of it is recommended.
#
# Two (maybe three) things need to be edited:
#
# 1. The name of the parameters needed for the calculation of Pk.
#    "sys.argv[1]" corresponds to "custom1" in Class, an so on
#
# Adding knotted functionality as in 1606.03057

try :
    k_0           = float(sys.argv[1])
    A             = float(sys.argv[2])
    n_s           = float(sys.argv[3])
    A_kmid        = float(sys.argv[4])

# Error control, no need to touch
except IndexError :
    raise IndexError("It seems you are calling this script with too few arguments.")
except ValueError :
    raise ValueError("It seems some of the arguments are not correctly formatted. "+
                     "Remember that they must be floating point numbers.")

#Limits for k and resolution
log_k_min  = -6
log_k_max  = 1
k_per_decade_primordial = 200
N_k = k_per_decade_primordial*(log_k_max-log_k_min) + 1

# Defining the fiducial Pk
def P(k):
    return A * (k/k_0)**(n_s-1.)

#filling the array of k's
k_array = np.logspace(log_k_min,log_k_max,N_k)

# Defining knot positions
log_k_knots = [log_k_min,-3,log_k_max]

# Defining knot values
log_A_knots = [0.,A_kmid,0.]

# Doing the interpolation
f = interp1d(log_k_knots,log_A_knots)

# Filling the array of Pk's
for k in k_array :
    P_k = P(k)*10**f(np.log10(k))
    print("%.18g %.18g" % (k, P_k))

#print (k_array,P(k_array)*10**f(np.log10(k_array)))