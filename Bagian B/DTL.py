from abc import ABC, abstractmethod
from math import log2
import pandas

class Node:

    def __init__(self, instances, targets, target=None):
        self.rule_children = {}     #dictionary yang berisi string (rule) sebagai key-nya dan objek Node sebagai valuenya
        self.target = target          #nilai target jika ada (untuk node-node daun)
        self.instances = instances  #array yang menyimpan instans
        self.targets = targets      #array yang menyimpan target
        self.entropy = self.calc_entropy()

    def get_instances(self):
        return self.instances

    def get_targets(self):
        return self.targets

    def get_target(self):
        return self.target

    def get_entropy(self):
        return self.entropy

    def get_rule_children(self):
        return self.rule_children
    
    def next_node(self, X):
        for rule in self.rule_children.keys():
            if eval(rule):
                return self.rule_children[rule]
        return Node([], [])
            
    def set_rule_children(self, str_rules, children_nodes):
        for i, str_rule in enumerate(str_rules):
            self.rule_children[str_rule] = children_nodes[i]

    def calc_entropy(self):
        s = len(self.instances) #Banyaknya instans
        sv = {}                 #Menyimpan banyaknya instans dari kelas tertentu
        entropy = 0             #Variabel sum

        for target in self.targets:
            if target in sv.keys():
                sv[target] += 1
            else:
                sv[target] = 1

        for target in self.targets:
            p = sv[target]/s
            entropy += -1*(p)*log2(p)

        return entropy



class DecisionTree(ABC):

    @abstractmethod
    def fit(self, instances, targets):
        pass
    @abstractmethod
    def predict(self, instances):
        pass

    def read_csv(self, file): # file dalam string
        csvFile = pandas.read_csv(file)
        return csvFile
    
    def information_gain(self, parent_node, children_nodes):
        info_gain = parent_node.get_entropy()
        
        num_parent_instance = len(parent_node.get_instances())
        num_childrens = len(children_nodes) # ?

        for i in range(num_childrens):
            num_children_targets = len(children_nodes[i].get_targets())
            info_gain -= abs(num_children_targets) * children_nodes[i].get_entropy() / abs(num_parent_instance)

        return info_gain