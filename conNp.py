import numpy as np
import math
A=np.array([0.25,0.15,0],[0.45,0.5,0.75],[0.3,0.35,0.25])
B=np.array([1.5,5,3])
X=np.linalg.solve(A,B)
print(X)
