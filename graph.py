from typing import Coroutine
from node import Node
from edge import Edge

class Graph:
    __total_edges = 0
    __total_nodes = 0
    def __init__(self ,oriented : bool):
        self.nodes = dict()
        self.edges = dict()
        self.oriented = oriented

    def add_node(self ,id ,data):
        if id not in self.nodes:
            self.nodes[id] = Node(id,data)
            self.__total_nodes += 1
        else:
            print("this id is allready associated with an other node")
    
    def add_edge(self ,node_start ,node_end ,value = 0):
        if (node_start,node_end) not in self.edges:
            self.edges[(node_start,node_end)] = Edge(node_start ,node_end,value,self.oriented)
            self.__total_edges += 1
        if node_start not in self.nodes or node_end not in self.nodes:
            print("one (or both) of the node doesn't exist yet !!")
    def __str__(self):
        result =f'---------- Graph: node={self.__total_nodes} edge={self.__total_edges} -----------\n'
        for edge in self.edges.values():
            result += str(self.nodes[edge.node_start])+str(edge)+str(self.nodes[edge.node_end])+"\n"
        return result+"-------------------------------------------"
    
    def remove_edge(self,node_start,node_end):
        if (node_start,node_end) in self.edges:
            del self.edges[(node_start,node_end)]
            self.__total_edges -= 1
        
    def remove_node(self,id_node):
        if id_node in self.nodes:
            list =[]
            for edge in self.edges:
                if id_node in edge:
                    list.append(edge)
            for edge in list:
                self.remove_edge(edge[0],edge[1])
            del self.nodes[id_node]
            self.__total_nodes -= 1

    

graph = Graph(True)
graph.add_node(1,"rachid")
graph.add_node(2,"alli")
graph.add_node(3,"mouhamed")
graph.add_edge(1,2,3)
graph.add_edge(2,3,5)
print(graph)
graph.remove_node(1)
print(graph)

