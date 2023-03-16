
class Node:

    def __init__(self, type, value):
        self.type = type
        self.value = value


class Stave:
    
    def __init__(self):
        self.nodes = []
        self.Bpm = 0

    def AddNode(self, node):
        self.nodes.append(node)
    
    def GetNodes(self):
        return self.nodes