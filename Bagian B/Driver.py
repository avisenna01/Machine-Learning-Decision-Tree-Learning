import pandas
from DTL import Node
from ID3 import id3 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load Datasets
label_encoder = preprocessing.LabelEncoder()
iris_datasets = load_iris()
tennisData = pandas.read_csv("play_tennis.csv")

# Node testing
instances = [[0, 1, 2], [2, 1, 0]]
targets = [1, 0]
rules = ["== 0"]
root = Node(0, instances, targets)

nodes = [Node(1, [instances[0]], [targets[0]])]
root.set_rule_children(rules, nodes)
child = root.next_node(instances[0])
child.set_rule_children(["== 1"], [Node([instances[1]], [targets[1]])])

some_child = root.next_node(instances[0])
# print(some_child.rule_children)

tennisAttr = []
tennisTarget = tennisData['play'].values

tennisOutlook = tennisData['outlook'].values
tennisTemp = tennisData['temp'].values
tennisHumidity = tennisData['humidity'].values 
tennisWind = tennisData['wind'].values

for i in range(len(tennisData)):
    tennisAttr.append([tennisOutlook[i], tennisTemp[i], tennisHumidity[i], tennisWind[i]])
    
tennisTrain, tennisTest, targetTrain, targetTest = train_test_split(tennisAttr, tennisTarget, test_size=0.1, random_state=42)


id = id3(instances,targets)
# id.fit(id.instances,id.targets)
id.fit(tennisTrain,targetTrain)

# makan[0] = node1
# makan[1] = node2
# makan[3] = node3