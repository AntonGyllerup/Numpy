import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
import scipy.optimize as optimize
from scipy.integrate import solve_ivp
import requests

#vi importerar nedan in data

text = requests.get("https").text
#spara till fil
with open("filnam.txt", "w") as f:
    f.write(text)
