from math import log2
import pandas

class Node:

    def __init__(self, attribute=None, instances=[], targets=[]):
        self.rule_children = {}     #dictionary yang berisi string (rule) sebagai key-nya dan objek Node sebagai valuenya
        self.attribute = attribute  #integer, index atribut yang dicek pada node tersebut, index dimulai dari 0
        self.instances = instances  #array yang menyimpan instans
        self.targets = targets      #array yang menyimpan target
        self.entropy = self.calc_entropy()
    
    def next_node(self, X):
        if self.attribute != None:
            for rule in self.rule_children.keys():
                if eval("X[" + str(self.attribute) + "] " + rule):
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

class DecisionTree():

    def __init__(self, arr_instans, arr_target):
        self.instances = arr_instans
        self.target = arr_target

    def fit(self, instances, targets):
        pass
    
    def predict(self, instances):
        pass

    # def read_csv(self, file): # file dalam string
    #     csvFile = pandas.read_csv(file)
    #     return csvFile
    
    def information_gain(self, parent_node, children_nodes):
        info_gain = parent_node.get_entropy()
        
        num_parent_instance = len(parent_node.get_instances())
        num_childrens = len(children_nodes) # ?

        for i in range(num_childrens):
            num_children_targets = len(children_nodes[i].get_targets())
            info_gain -= abs(num_children_targets) * children_nodes[i].get_entropy() / abs(num_parent_instance)

        return info_gain

    def getTrainColLength(self,arr_instans):
        count=0
        for i in arr_instans[0]:
            count+=1
        return count
    
    def getTrainRowLength(self,arr_instans):
        count=0
        for i in arr_instans:
            count+=1
        return count
        