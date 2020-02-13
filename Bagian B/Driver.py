import pandas
from DTL import Node
from ID3 import id3 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load Datasets
iris_datasets = load_iris()
tennis_datasets = pandas.read_csv("play_tennis.csv")

#pre-process tennis_datasets
label_encoder = preprocessing.LabelEncoder()
tennis_datasets = tennis_datasets[['outlook', 'temp', 'humidity', 'wind', 'play']]
for attribute in tennis_datasets:
    tennis_datasets[attribute] = label_encoder.fit_transform(tennis_datasets[attribute])

tennis_outlook = tennis_datasets['outlook'].values
tennis_temp = tennis_datasets['temp'].values
tennis_humidity = tennis_datasets['humidity'].values
tennis_wind = tennis_datasets['wind'].values

tennis_targets = tennis_datasets['play'].values
tennis_instances = []

for i in range(len(tennis_datasets)):
    tennis_instances.append([tennis_outlook[i],
                            tennis_temp[i],
                            tennis_humidity[i],
                            tennis_wind[i]])

#pre-process iris datasets
iris_instances = iris_datasets.data
iris_targets = iris_datasets.target

id = id3(tennis_instances,tennis_targets)
id.fit(id.instances,id.targets)

# Node testing
""" instances = [[0, 1, 2], [2, 1, 0]]
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
print(some_child.rule_children) """
