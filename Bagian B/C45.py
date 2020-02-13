import os
import pandas
from DTL import DecisionTree, Node
from math import log2
from icecream import ic
from ID3 import ID3

class C45(DecisionTree):

    def __init__(self, arr_instans, arr_target):
        DecisionTree.__init__(self, arr_instans, arr_target)

    def predict(self, instances):
        predictions = []
        for instance in instances:
            root = self.root
            while root.attribute != None:
                root = root.next_node(instance)
            predictions.append(root.target)
        return predictions

    def fit(self, arr_instans, arr_target):
        #convert array to dataframe
        df = pandas.DataFrame.from_records(arr_instans)
        arr_target = pandas.DataFrame(arr_target)
        arr_instans = df.assign(target = arr_target.values)

        ic(arr_instans)

        #pre-process continuous valued attribute
        arr_instans = self.continuous_value(arr_instans)

        #pre-process missing value attribute
        arr_instans = self.missing_value_handler(arr_instans)

        #pre-process attribute with many values

        #convert dataframe to array of array
        arr_target = [target[0] for target in arr_target.values]
        arr_instans = arr_instans.drop(columns="target", axis=1)
        arr_instans = arr_instans.values.tolist()

        #ic(arr_instans)
        #ic(arr_target)

        #buat objek ID3
        id3_ = ID3(arr_instans, arr_target)

        #fitting ID3
        id3_.fit(arr_instans, arr_target)

        #this->root = ID3.root
        self.root = id3_.root

    @staticmethod
    def target_most_common_attribute(training_data):

        target_name = training_data.columns[-1] #name of target attribute
        res = []
        dict = {}
        for i in training_data[target_name].unique():
            res.append(training_data.loc[training_data[target_name] == i].mode().loc[0])
            dict[i] = training_data.loc[training_data[target_name] == i].mode().loc[0]

        return dict

    def missing_value_handler(self, training_data):

        most_common_att = C45. target_most_common_attribute(training_data)
        attribute_name = training_data.columns[:-1]
        target_name = training_data.columns[-1]


        for att in attribute_name:
            indexes = training_data.index[training_data[att] == "None"].tolist()

            for id in indexes:
                print(training_data[target_name][id])
                training_data[att][id] = most_common_att[training_data[target_name][id]][att]

        
        return training_data

    def continuous_value(self, training_data):

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
            sorted[att][:split_point] = int(0)
            sorted[att][split_point:] = int(1)

            final_dataset = sorted
    
        return final_dataset.astype(int)

    @staticmethod
    def entrophy(dataset):
        total_value = len(dataset)
        target_name = dataset.columns[-1]
        value_count = dataset[target_name].value_counts()

        res = 0
        for i in value_count:

            res = res - i/total_value * log2(i/total_value)

        return res







        





""" #Load Datasets
#print(tennisData.columns[-1])

iris = load_iris()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test.csv')
tennisData = pandas.read_csv(filename)

df = pandas.DataFrame.from_records(iris.data)
iris_targets = pandas.DataFrame(iris.target)

iris_data = df.assign(target = iris_targets.values)

print(tennisData)

print(tennisData.index[tennisData['play'] == "Yes"].tolist())

print(C45.target_most_common_attribute(tennisData))
print(C45.missing_value_handler(tennisData))

print(C45.continuous_value(iris_data))
 """