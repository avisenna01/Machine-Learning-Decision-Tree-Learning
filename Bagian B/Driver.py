import pandas
from DTL import Node
from sklearn import preprocessing
from sklearn.datasets import load_iris

# Load Datasets
label_encoder = preprocessing.LabelEncoder()
iris_datasets = load_iris()
tennis_datasets = pandas.read_csv("play_tennis.csv")

""" # Node testing
instances = [[0, 1, 2], [2, 1, 0]]
targets = [1, 0]
rules = ["X[0] == 0"]
root = Node(instances, targets)

nodes = [Node([instances[0]], [targets[0]], targets[0])]
root.set_rule_children(rules, nodes)
child = root.next_node(instances[0])
child.set_rule_children(["X[1] == 1"], [Node([instances[1]], [targets[1]], targets[1])])

some_child = root.next_node(instances[0])
print(some_child.get_rule_children()) """


