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
        sv = dict()         #Menghitung banyaknya instans dari kelas tertentu
        entropy = 0         #Variabel sum

        for target in arr_target:
            sv[target] += 1

        for target in arr_target:
            p = s/sv
            entropy += -1*(p)*log2(p)

        return entropy
    
    

