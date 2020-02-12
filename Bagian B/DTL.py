from abc import ABC, abstractmethod
from math import log2
import pandas

class DecissionTree(ABC):

    @abstractmethod
    def fit(self, arr_instans, arr_target):
        pass
    @abstractmethod
    def predict(self, arr_instans):
        pass

     def read_csv(self, file): # file dalam string
        csvFile = pandas.read_csv(file)
        return csvFile

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
    
    def gain(self, entropy, data_train): # assume

        row = len(data_train)
        col = len(data_train[0])

        for j in range(col):
            for i in range(col[j])

        entropy_calculation = 
        return entropy - entropy_calculation
        

    

