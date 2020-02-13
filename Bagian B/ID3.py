from DTL import DecisionTree, Node
from icecream import ic
# from DTL import Node

class id3(DecisionTree):
    def __init__(self, arr_instans, arr_target):
        DecisionTree.__init__(self, arr_instans, arr_target)
        self.instances = arr_instans
        self.targets = arr_target
        self.root = None

    def predict(self, instances):
        predictions = []
        for instance in instances:
            root = self.root
            while root.attribute != None:
                root = root.next_node(instance)
            predictions.append(root.target)
        return predictions

    def fit(self, arr_instans, arr_target):
        node_p = Node(instances=arr_instans,targets=arr_target)
        
        if (node_p.entropy==0):
            node_p.target = node_p.calc_target()
            node_p.print_node()

            return node_p
        else:

            row = self.getTrainRowLength(arr_instans)
            col = self.getTrainColLength(arr_instans)

            #mencari atribut terbaik dari instans
            max_gain = 0 # value gain
            node_p.attribute = 0 # index col gain idx_gain

            """ ic(arr_instans)
            ic(arr_target) """

            for j in range(col):
                dict_attrval_targets = {}

                for i in range(row):
                    # ic(arr_instans[i])
                    curr_val = arr_instans[i][j]
                    if curr_val in dict_attrval_targets.keys():
                        dict_attrval_targets[curr_val].append(arr_target[i])
                    else:
                        dict_attrval_targets[curr_val] = [arr_target[i]]
                gain = self.information_gain(node_p.entropy, len(arr_instans), dict_attrval_targets.values())
                """ ic(dict_attrval_targets)
                ic(dict_attrval_targets.values())
                ic(gain)
                ic(node_p.attribute) """

                if (max_gain < gain):
                    max_gain = gain
                    node_p.attribute = j

            #membentuk list rules dan membagi instances dan targets kedalam children nodesnya
            rules = []
            attr_val = []
            new_instances_targets = {}

            for i, instance in enumerate(arr_instans):
                curr_val = instance[node_p.attribute]

                if curr_val not in attr_val:
                    attr_val.append(curr_val)
                    rules.append(" == " + str(curr_val))

                if curr_val not in new_instances_targets.keys():
                    new_instances_targets[curr_val] = [[instance], [arr_target[i]]]
                else:
                    new_instances_targets[curr_val][0].append(instance)
                    new_instances_targets[curr_val][1].append(arr_target[i])

            """ ic(rules)
            ic(attr_val)
            ic(new_instances_targets) """

            #membentuk node childrennya
            childrens = []
            for instances_targets in new_instances_targets.values():
                #ic(instances_targets)
                childrens.append(self.fit(instances_targets[0], instances_targets[1]))

            #set rules children untuk nope_p
            node_p.set_rule_children(rules, childrens)
            node_p.print_node()


            """ temp_instans = arr_instans
            temp_target = arr_target
            length = len(temp_instans) # panjang list temp instans

            list_att_val = []
            # while len(temp_instans)>0:
            for i in range(row):
                if temp_instans[i][node_p.attribute] not in list_att_val:
                    list_att_val.append(temp_instans[i][node_p.attribute])
                
            l = len(list_att_val)
            list_node = []
            list_rules = []

            for val_idx in range(l):
                children_instans = []
                children_target_instans = []

                for i in range(length):
                    if (temp_instans[i][node_p.attribute]==list_att_val[val_idx]):    
                        children_instans.append(temp_instans[i])
                        children_target_instans.append(temp_target[i])
                #         print("test1")
                #     print("test2")
                # print("test3")
                list_node.append(self.fit(children_instans, children_target_instans))
                list_rules.append("== "+str(val_idx))
            
            print(list_rules)
            print(list_node)
            node_p.set_rule_children(list_rules,list_node)
            node_p.print_node() """

            self.root = node_p

            return node_p