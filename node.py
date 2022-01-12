class Node:
    def __init__(self,id : int,data :str):
        self.id = id
        self.data = data
    def set_data(self ,new_data):
        self.data = new_data
    def get_data(self):
        return self.data
    def __str__(self):
        return self.data