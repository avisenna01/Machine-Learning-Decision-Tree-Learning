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

    def target_most_common_attribute(training_data):
        yes = training_data.loc[tennisData['play'] == 'Yes']
        no = training_data.loc[tennisData['play'] == 'No']

        return (yes.mode().loc[0], no.mode().loc[0])

    def continuous_value(training_data, list_col, arr_target, node_p):
        sorted = training_data.sort_values(by=['outlook'])
       
        
        candidate_index = []
        for x in range(len(sorted)):
            current_target = sorted['play'].iloc[x] #nilai target saat ini

            if not(x==1):
                if not(sorted['play'].iloc[x-1] == sorted['play'].iloc[x]):
                    candidate_index.append(x)
                 
        print(sorted)
        print(candidate_index)

        return 1



#Load Datasets
iris = load_iris()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.csv')
tennisData = pandas.read_csv(filename)
print(tennisData)

tt = C45.continuous_value(tennisData)
print(tt)


