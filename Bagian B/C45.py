#from DTL import DecissionTree

# class C45(DecissionTree):
#     def post_prune(self):
#         return null

#     def target_most_common_attribute(self):
#         return null
import os
import pandas
from sklearn import preprocessing
import sklearn.datasets as dataset

# Load Datasets
data = pandas.read_csv(r"test.csv")
print(data)
