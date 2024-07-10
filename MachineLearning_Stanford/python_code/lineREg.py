import matplotlib
import numpy as np
from sklearn import datasets, linear_model


diab=datasets.load_diabetes()
# print(diab.keys())
print(diab.DESCR)
# diab_X=