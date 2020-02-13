from DTL import DecisionTree, Node
import os
import pandas
from sklearn import preprocessing
from sklearn.datasets import load_iris
import math

class C45():

    def post_prune(self):
        return None

    def target_most_common_attribute(training_data):

        target_name = training_data.columns[-1] #name of target attribute
        res = []
        for i in training_data[target_name].unique():
            res.append(training_data.loc[training_data[target_name] == i].mode().loc[0])

        return res

    def continuous_value(training_data):

        attribute_name = training_data.columns[:-1]
        target_name = training_data.columns[-1]

        final_dataset = training_data

        
        for att in attribute_name:


            sorted = final_dataset.sort_values(by=[att])
        
            
            candidate_index = []
            for x in range(len(sorted)):
                current_target = sorted[target_name].iloc[x] #nilai target saat ini

                if not(x==1):
                    if not(sorted[target_name].iloc[x-1] == sorted[target_name].iloc[x]):
                        candidate_index.append(x)
                    
            #print(candidate_index)

            information_gains = []

            for i in candidate_index:
                upper = sorted[:i]
                down = sorted[i:]
                #print(C45.entrophy(upper))
                information_gain =  len(upper)/len(training_data)*C45.entrophy(upper) + len(down)/len(training_data)*C45.entrophy(down)
                #print(information_gain)
                information_gains.append(information_gain)

            temp = information_gains.index(min(information_gains))

            #print(temp)

            split_point = candidate_index[temp]
            sorted[att][:split_point] = 0
            sorted[att][split_point:] = 1

            final_dataset = sorted
        return final_dataset

    def entrophy(dataset):
        total_value = len(dataset)
        target_name = dataset.columns[-1]
        value_count = dataset[target_name].value_counts()

        res = 0
        for i in value_count:

            res = res - i/total_value * math.log2(i/total_value)

        return res







        





#Load Datasets
#print(tennisData.columns[-1])

iris = load_iris()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.csv')
tennisData = pandas.read_csv(filename)

df = pandas.DataFrame.from_records(iris.data)
iris_targets = pandas.DataFrame(iris.target)

iris_data = df.assign(target = iris_targets.values)



tt = C45.continuous_value(iris_data)

print(tt)


