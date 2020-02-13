from DTL import DecisionTree, Node
import os
import pandas
from sklearn import preprocessing
from sklearn.datasets import load_iris

class C45(DecisionTree):

    def __init__(self, arr_instans, arr_target):
        DecisionTree.__init__(self, arr_instans, arr_target)
        self.instances = arr_instans
        self.targets = arr_target
        print(self.targets)

    def post_prune(self):
        return null

    def target_most_common_attribute(self):
        return null



# Load Datasets

# iris = load_iris()

# #print(iris)

# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, 'test.csv')
# tennisData = pandas.read_csv(filename)
# print(tennisData)
# # t =  tennisData.mode(axis = 5)
# # print(t)

# yes = tennisData.loc[tennisData['play'] == 'Yes']
# no = tennisData.loc[tennisData['play'] == 'No']


# print(tennisData.mode().loc[0][1])