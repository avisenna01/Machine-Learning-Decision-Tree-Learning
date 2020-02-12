from abc import ABC, abstractmethod
from math import log2

class DecissionTree(ABC):

    @abstractmethod
    def fit(self, arr_instans, arr_target):
        pass
    @abstractmethod
    def predict(self, arr_instans):
        pass

    def entropy(self, arr_target):
        s = len(arr_target) #Banyaknya instans
        sv = [0]*s          #Menyimpan banyaknya instans dari kelas tertentu
        entropy = 0         #Variabel sum

        for target in arr_target:
            sv[target] += 1

        for target in arr_target:
            p = s/sv[target]
            entropy += -1*(p)*log2(p)

        return entropy

    def information_gain(self, arr_parent_target, arr_childrens_target):
        info_gain = self.entropy(arr_parent_target)
        
        num_parent_instance = len(arr_parent_target)
        num_childrens = len(arr_childrens_target)

        for i in range(num_childrens):
            info_gain -= abs(num_parent_instance)*self.entropy(arr_childrens_target[i])/abs(len(arr_childrens_target[i]))

        return info_gain
