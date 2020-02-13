from DTL import DecisionTree, Node
# from DTL import Node

class id3(DecisionTree):
    def __init__(self, arr_instans, arr_target):
        self.arr_instans = arr_instans
        self.arr_target = arr_target

    def id3(self, arr_instans, arr_target):
        n = Node(arr_instans,arr_target)

        row = super.getTrainRowLength(arr_instans)
        col = super.getTrainColLength(arr_instans)

        max_gain = 0 # value gain
        idx_gain = 0 # index col gain
       
        for j in range(col):
            list_col = []
            for i in range(row):
                list_col.append(arr_instans[i][j])

            gain = super.information_gain(list_col,arr_target)

            if (max_gain < gain):
                max_gain = gain
                idx_gain = j

        temp_instans = arr_instans
        temp_target = arr_target
        length = len(temp_instans) # panjang list temp instans

        list_att_val = []
        # while len(temp_instans)>0:
        for i in range(row):
            if temp_instans[i][idx_gain] not in list_att_val:
                list_att_val.append(temp_instans[i][idx_gain])
            
        l = len(list_att_val)

        for val_idx in range(l):
            children_instans = []
            children_target_instans = []

            for i in range(length):
                if (temp_instans[i][idx_gain]==list_att_val[val_idx]):    
                    children_instans.append(temp_instans[i])
                    children_target_instans.append(temp_target[i])

            id3(children_instans, children_target_instans)
                        

        
        
