from abc import ABC, abstractmethod

class DecissionTree(ABC):

    @abstractmethod
    def fit(self, arr_instans, arr_target):
        pass
    @abstractmethod
    def predict(self, arr_instans):
        pass
