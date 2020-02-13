from math import log2
import pandas

class Node:

    def __init__(self, attribute=None, instances=[], targets=[]):
        self.rule_children = {}     #dictionary yang berisi string (rule) sebagai key-nya dan objek Node sebagai valuenya
        self.attribute = attribute  #integer, index atribut yang dicek pada node tersebut, index dimulai dari 0
        self.instances = instances  #array yang menyimpan instans
        self.targets = targets      #array yang menyimpan target
        self.entropy = DecisionTree.entropy(targets)
        self.target = None
    
    def next_node(self, X):
        if self.attribute != None:
            for rule in self.rule_children.keys():
                if eval("X[" + str(self.attribute) + "] " + rule):
                    return self.rule_children[rule]
        
        return Node()
            
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

    def calc_target(self):
        num = {}

        for target in self.targets:
            if target not in num.keys():
                num[target] = 0
            else:
                num[target] += 1

        max_num = 0
        final_target = None
        for target, val in num.items():
            if val >= max_num:
                max_num = val
                final_target = target

        return final_target 

    def print_node(self):
        print("RULE_CHILDREN ->",self.rule_children)
        print("ATTRIBUTE ->",self.attribute)
        print("INSTANCES ->",self.instances)
        print("TARGETS ->",self.targets)
        print("ENTROPI ->" , self.entropy)
        print("TARGET ->", self.target, "\n")

class DecisionTree():

    def __init__(self, arr_instans, arr_target):
        self.instances = arr_instans
        self.targets = arr_target
        self.root = None

    def fit(self, instances, targets):
        pass
    
    def predict(self, instances):
        pass

    @staticmethod
    def entropy(targets):
        s = len(targets) #Banyaknya instans
        sv = {}                 #Menyimpan banyaknya instans dari kelas tertentu
        entropy = 0             #Variabel sum

        for target in targets:
            if target in sv.keys():
                sv[target] += 1
            else:
                sv[target] = 1

        for target in targets:
            p = sv[target]/s
            entropy += -1*(p)*log2(p)

        return entropy

    @staticmethod
    def information_gain(parent_ent, S,  list_targets):
        gain = parent_ent

        for targets in list_targets:
            gain -= len(targets)*DecisionTree.entropy(targets)/S

        return gain
    
    @staticmethod
    def getTrainColLength(arr_instans):
        count=0
        for i in arr_instans[0]:
            count+=1
        return count
    
    @staticmethod
    def getTrainRowLength(arr_instans):
        count=0
        for i in arr_instans:
            count+=1
        return count
        