from DTL import DecisionTree, Node
# from DTL import Node

class id3(DecisionTree):
    def __init__(self, arr_instans, arr_target, root=None):
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
        predictions += [root.calc_entropy()]
        return predictions

    def fit(self, arr_instans, arr_target):
        node_p = Node(instances=arr_instans,targets=arr_target)
        
        if (node_p.entropy==0):
            node_p.print_node()
            return node_p
        else:

            row = self.getTrainRowLength(arr_instans)
            col = self.getTrainColLength(arr_instans)

            max_gain = 0 # value gain
            node_p.attribute = 0 # index col gain idx_gain

            for j in range(col):
                list_col = []
                for i in range(row):
                    list_col.append(arr_instans[i][j])

                gain = self.information_gain(list_col,arr_target, node_p)

                if (max_gain < gain):
                    max_gain = gain
                    node_p.attribute = j

            temp_instans = arr_instans
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
            node_p.print_node()
            self.root = node_p
            return node_p