import pandas
import os
from DTL import Node
from C45 import C45 as c_45
from sklearn import preprocessing
from sklearn.datasets import load_iris

[["Sunny","Hot","High","Weak","No"],
["Sunny","Hot","High","Strong","No"],
["Overcast","Hot","High","Weak","Yes"],
["Rain","Mild","High","Weak","Yes"],
["Rain","Cool","Normal","Weak","Yes"],
["Rain","Cool","Normal","Strong","No"],
["Overcast","Cool","Normal","Strong","Yes"],
["Sunny","Mild","High","Weak","No"],
["Sunny","Cool","Normal","Weak","Yes"],
["Rain","Mild","Normal","Weak","Yes"],
["Sunny","Mild","Normal","Strong","Yes"],
["Overcast","Mild","High","Strong","Yes"],
["Overcast","Hot","Normal","Weak","Yes"],
["Rain","Mild","High","Strong","No"]]

# Load Datasets
label_encoder = preprocessing.LabelEncoder()
iris_datasets = load_iris()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'play_tennis.csv')
tennis_datasets = pandas.read_csv(filename)

# Node testing
instances = [[0, 1, 2], [2, 1, 0]]
targets = [1, 0]
rules = ["== 0"] #rules
root = Node(0, instances, targets)

nodes = [Node(1, [instances[0]], [targets[0]])]
root.set_rule_children(rules, nodes)



child = root.next_node(instances[0])
child.set_rule_children(["== 1"], [Node([instances[1]], [targets[1]])])

some_child = root.next_node(instances[0])
print(some_child.rule_children)

id = c_45(instances,targets)
#id.fit(id.instances,id.targets)

# makan[0] = node1
# makan[1] = node2
# makan[3] = node3


