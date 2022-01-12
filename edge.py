class Edge:
    def __init__(self,node_start :int ,node_end :int ,value :str ,oriented = True):
        self.node_start = node_start
        self.node_end = node_end
        self.value = value
        self.oriented = oriented
    
    def set_value(self ,new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_type_orientation(self):
        return self.oriented
    
    
    def __str__(self):
        if self.oriented:
            return "----------"+str(self.value)+"--------->"
        else:
            return "----------"+str(self.value)+"----------"
