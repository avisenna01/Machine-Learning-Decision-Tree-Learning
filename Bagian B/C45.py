from DTL import DecisionTree, Node
import os
import pandas
from sklearn import preprocessing
from sklearn.datasets import load_iris

class C45():

    def post_prune(self):
        return null

    def target_most_common_attribute(training_data,att_name):
        yes = training_data.loc[training_data[att_name] == 'Yes']
        no = training_data.loc[training_data[att_name] == 'No']

        return (yes.mode().loc[0], no.mode().loc[0])

    def continuous_value(training_data,att_name):
        sorted = training_data.sort_values(by=['outlook'])
       
        
        candidate_index = []
        for x in range(len(sorted)):
            current_target = sorted[att_name].iloc[x] #nilai target saat ini

            if not(x==1):
                if not(sorted[att_name].iloc[x-1] == sorted[att_name].iloc[x]):
                    candidate_index.append(x)
                 
        print(sorted)
        print(candidate_index)

        return 1





#Load Datasets
iris = load_iris()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.csv')
tennisData = pandas.read_csv(filename)

df = pandas.DataFrame.from_records(iris.data)
iris_targets = pandas.DataFrame(iris.target)

iris_data = df.assign(target = iris_targets.values)
print(iris_data)

tt = C45.continuous_value(tennisData,tennisData.columns[-1])
print(tt)


