from math import log2
import pandas

class Node:

    def __init__(self, attribute=None, instances=[], targets=[]):
        self.rule_children = {}     #dictionary yang berisi string (rule) sebagai key-nya dan objek Node sebagai valuenya
        self.attribute = attribute  #integer, index atribut yang dicek pada node tersebut, index dimulai dari 0
        self.instances = instances  #array yang menyimpan instans
        self.targets = targets      #array yang menyimpan target
        self.entropy = self.calc_entropy()
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
        self.target = arr_target

    def fit(self, instances, targets):
        pass
    
    def predict(self, instances):
        pass

    # def read_csv(self, file): # file dalam string
    #     csvFile = pandas.read_csv(file)
    #     return csvFile
    
    # def information_gain(self, parent_node, children_nodes):
    #     info_gain = parent_node.get_entropy()
        
    #     num_parent_instance = len(parent_node.get_instances())
    #     num_childrens = len(children_nodes) # ?

    #     for i in range(num_childrens):
    #         num_children_targets = len(children_nodes[i].get_targets())
    #         info_gain -= abs(num_children_targets) * children_nodes[i].get_entropy() / abs(num_parent_instance)

    #     return info_gain

    # def information_gain(self, parent_node, children_nodes):
    #     info_gain = parent_node.entropy
        
    #     num_parent_instance = len(parent_node.instances)
    #     num_childrens = len(children_nodes) # ?

    #     for i in range(num_childrens):
    #         num_children_targets = len(children_nodes[i].targets)
    #         info_gain -= abs(num_children_targets) * children_nodes[i].entropy / abs(num_parent_instance)

    #     return info_gain

    def information_gain(self, list_col, arr_target, node_p):
        ent = node_p.entropy
        ratio = len(list_col)
        l = []
        l_sum = []
        for i in list_col:
            if i not in l:
                l.append(i)
                l_sum.append(1)
            else:
                for j in range(len(l)):
                    if (i == l[j]):
                        l_sum[j]+=1
                        break
        att_total = len(l) # total atribut
        for i in range(att_total):
            ins = []
            tgt = []
            for j in range(ratio):
                if (list_col[j]==l[i]):
                    ins.append(list_col[j])
                    tgt.append(arr_target[j])
            n_temp = Node(instances=ins,targets=tgt)
            ent-= (l_sum[i]/ratio)*n_temp.entropy
        
        return ent
    
    def split_information(self, list_col, arr_target, node_p):
        r = 0
        ratio = len(list_col)
        l = []
        l_sum = []
        for i in list_col:
            if i not in l:
                l.append(i)
                l_sum.append(1)
            else:
                for j in range(len(l)):
                    if (i == l[j]):
                        l_sum[j] += 1
                        break
        att_total = len(l)
        for i in range(att_total):
            r -= (l_sum[i]/ratio)*log2(l_sum[i]/ratio)
        return r


    def gain_ratio(self, list_col, arr_target, node_p):
        return information_gain(list_col, arr_target, node_p) / split_information(list_col, arr_target, node_p)

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
        