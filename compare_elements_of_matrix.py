import numpy as np

A= np.random.normal(size=(5,20)) 
B= np.zeros((5,20))
print(np.maximum(A,B))
