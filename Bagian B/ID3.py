from .DTL.py import DecissionTree

class id3(DecissionTree):
    def __init__(self, arr_instans, arr_target):
        self.arr_instans = arr_instans
        self.arr_target = arr_target

    def id3(self):
        ent = DTL.entropy(self.arr_target) # entropi node

        for 

        
